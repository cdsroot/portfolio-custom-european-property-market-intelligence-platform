# Data Governance

This project separates official transaction intelligence from later listing
intelligence. It does not scrape real-estate listing portals.

## French DVF Handling

- Do not store owner names.
- Do not expose exact addresses publicly.
- Do not publish exact property records as search-engine-indexable pages.
- Keep exact coordinates only in protected analytical storage.
- Publish municipality-level or otherwise aggregated outputs where possible.
- Keep raw files immutable and record a manifest for each source file.
- Preserve rejected records in later normalization steps for auditability.

## Public Surfaces

Public dashboards should use aggregation, approximate spatial cells, and
municipality-level summaries. Public pages should describe methods and limits
instead of exposing record-level transaction search.

## Personal Data Principles

The project applies purpose limitation, data minimization, storage limitation,
and transparency. Later country adapters must be reviewed separately because
license terms, address fields, and reuse rights differ across official sources.
