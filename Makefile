.PHONY: install postgres-up postgres-ps download-dvf lint

install:
	pip install -e ".[dev]"

postgres-up:
	docker compose up -d

postgres-ps:
	docker compose ps

download-dvf:
	python -m property_intelligence.ingestion.download_dvf

lint:
	ruff check src
