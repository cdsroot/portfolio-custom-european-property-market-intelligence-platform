# Architecture

The first implementation is a France-only transaction-intelligence pipeline.

```text
data.gouv.fr DVF API
        |
        v
download_dvf.py
        |
        v
immutable CSV.GZ + manifest
        |
        v
future normalization to Parquet
        |
        v
future PostGIS load and feature generation
```

The project keeps source files immutable and records a manifest per source file.
Later stages will use Parquet for analytical storage, DuckDB for exploratory
queries, and PostgreSQL/PostGIS for protected spatial analytics.

PostGIS initialization SQL is mounted through `docker-compose.yml`, so schema
scripts run when the database volume is first created.
