from __future__ import annotations

import hashlib
import json
from datetime import UTC, datetime
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Any

import requests

from property_intelligence.config import get_settings

DATASET_API = "https://www.data.gouv.fr/api/1/datasets/demandes-de-valeurs-foncieres-geolocalisees/"


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()

    with path.open("rb") as file:
        while chunk := file.read(chunk_size):
            digest.update(chunk)

    return digest.hexdigest()


def package_version() -> str:
    try:
        return version("european-property-intelligence")
    except PackageNotFoundError:
        return "unknown"


def get_latest_csv_resource() -> dict[str, Any]:
    response = requests.get(DATASET_API, timeout=60)
    response.raise_for_status()

    metadata = response.json()

    candidates = [
        resource
        for resource in metadata["resources"]
        if str(resource.get("format", "")).lower() in {"csv.gz", "gz"} and resource.get("url")
    ]

    if not candidates:
        raise RuntimeError("No downloadable DVF CSV.GZ resource was found.")

    return max(
        candidates,
        key=lambda resource: resource.get("last_modified") or resource.get("modified") or "",
    )


def download_file(url: str, destination: Path) -> dict[str, str]:
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_suffix(destination.suffix + ".part")

    with requests.get(url, stream=True, timeout=(30, 600)) as response:
        response.raise_for_status()
        headers = dict(response.headers)

        with temporary.open("wb") as file:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    file.write(chunk)

    temporary.replace(destination)
    return headers


def build_manifest(
    *,
    resource: dict[str, Any],
    destination: Path,
    retrieved_at: datetime,
    http_headers: dict[str, str],
    ingestion_status: str,
) -> dict[str, Any]:
    return {
        "dataset": "France DVF geolocated",
        "resource_id": resource.get("id", "unknown"),
        "source_url": resource["url"],
        "retrieved_at": retrieved_at.isoformat(),
        "source_last_modified": resource.get("last_modified") or resource.get("modified"),
        "file": str(destination),
        "size_bytes": destination.stat().st_size,
        "sha256": sha256_file(destination),
        "http_headers": http_headers,
        "software_version": package_version(),
        "ingestion_status": ingestion_status,
    }


def main() -> None:
    settings = get_settings()
    resource = get_latest_csv_resource()

    retrieved_at = datetime.now(UTC)
    resource_id = resource.get("id", "unknown")
    filename = f"dvf-geolocated-{resource_id}.csv.gz"
    destination = settings.data_dir / "raw" / "france_dvf" / filename

    http_headers: dict[str, str] = {}
    ingestion_status = "reused_existing_file"

    if not destination.exists():
        http_headers = download_file(resource["url"], destination)
        ingestion_status = "downloaded"

    manifest = build_manifest(
        resource=resource,
        destination=destination,
        retrieved_at=retrieved_at,
        http_headers=http_headers,
        ingestion_status=ingestion_status,
    )

    manifest_path = destination.with_suffix(destination.suffix + ".manifest.json")
    manifest_path.write_text(
        json.dumps(manifest, indent=2),
        encoding="utf-8",
    )

    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
