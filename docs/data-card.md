# Data Card

## France DVF Geolocated

- Source: data.gouv.fr dataset API for geolocated DVF transactions.
- Geography: France.
- Initial use: official transaction intelligence.
- Raw format: CSV.GZ.
- Storage: immutable raw file plus JSON manifest.
- Protected fields: exact coordinates are retained only for analytical storage.
- Public reporting: aggregate by municipality or broader spatial grouping.
- Refresh: source is replaced during official periodic updates.

The conservative modeling subset and rejection rules are added in later steps.
