CREATE TABLE IF NOT EXISTS property_transactions (
    transaction_key TEXT PRIMARY KEY,
    source_name TEXT NOT NULL,
    source_transaction_id TEXT NOT NULL,

    country_code CHAR(2) NOT NULL,
    currency_code CHAR(3) NOT NULL,

    sale_date DATE NOT NULL,
    sale_price NUMERIC(15, 2) NOT NULL,

    property_type TEXT NOT NULL,
    floor_area_m2 NUMERIC(10, 2),
    room_count INTEGER,
    land_area_m2 NUMERIC(12, 2),

    admin_level_1 TEXT,
    admin_level_2 TEXT,
    municipality_code TEXT,
    municipality_name TEXT,

    longitude DOUBLE PRECISION,
    latitude DOUBLE PRECISION,
    geom GEOMETRY(Point, 4326),

    source_file_sha256 TEXT NOT NULL,
    source_updated_at TIMESTAMPTZ,
    loaded_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    CONSTRAINT positive_sale_price CHECK (sale_price > 0),
    CONSTRAINT positive_floor_area
        CHECK (floor_area_m2 IS NULL OR floor_area_m2 > 0),
    CONSTRAINT valid_latitude
        CHECK (latitude IS NULL OR latitude BETWEEN -90 AND 90),
    CONSTRAINT valid_longitude
        CHECK (longitude IS NULL OR longitude BETWEEN -180 AND 180)
);

CREATE UNIQUE INDEX IF NOT EXISTS uq_source_transaction
ON property_transactions(source_name, source_transaction_id);

CREATE INDEX IF NOT EXISTS idx_transactions_sale_date
ON property_transactions(sale_date);

CREATE INDEX IF NOT EXISTS idx_transactions_municipality
ON property_transactions(country_code, municipality_code);

CREATE INDEX IF NOT EXISTS idx_transactions_property_type
ON property_transactions(property_type);

CREATE INDEX IF NOT EXISTS idx_transactions_geom
ON property_transactions USING GIST(geom);
