# Testing Strategy

Through step 8, the most important checks are:

- Package installation.
- Settings loading from `.env`.
- DVF dataset API discovery.
- SHA-256 checksum calculation.
- Manifest completeness.
- SQL syntax and PostGIS initialization through Docker.

Later stages add unit tests for normalization, validation, feature leakage,
model splitting, API contracts, and statistical regression.
