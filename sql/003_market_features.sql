CREATE TABLE IF NOT EXISTS market_features (
    country_code CHAR(2) NOT NULL,
    municipality_code TEXT NOT NULL,
    property_type TEXT NOT NULL,
    period_month DATE NOT NULL,

    transaction_count INTEGER NOT NULL,
    median_price_m2 NUMERIC(15, 2),
    median_price_m2_lag_1m NUMERIC(15, 2),
    rolling_median_price_m2_6m NUMERIC(15, 2),
    rolling_transaction_count_6m INTEGER,

    PRIMARY KEY (
        country_code,
        municipality_code,
        property_type,
        period_month
    )
);

CREATE INDEX IF NOT EXISTS idx_market_features_lookup
ON market_features (
    country_code,
    municipality_code,
    property_type,
    period_month DESC
);

CREATE TABLE IF NOT EXISTS model_predictions (
    prediction_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    model_name TEXT NOT NULL,
    model_version TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    country_code CHAR(2) NOT NULL,
    municipality_code TEXT,
    property_type TEXT NOT NULL,

    predicted_price_m2 NUMERIC(15, 2) NOT NULL,
    lower_price_m2 NUMERIC(15, 2),
    upper_price_m2 NUMERIC(15, 2),

    input_features JSONB NOT NULL,
    actual_price_m2 NUMERIC(15, 2)
);
