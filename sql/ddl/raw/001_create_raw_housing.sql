-- =========================================
-- File: 001_create_raw_housing.sql
-- Description: Criação da tabela raw_housing
-- =========================================

CREATE TABLE IF NOT EXISTS raw_housing (

    --=========================================
    -- Primary key
    --=========================================
    id BIGSERIAL PRIMARY KEY,

    --=========================================
    -- Original Dataset Columns
    --=========================================
    longitude DOUBLE PRECISION NOT NULL,
    latitude DOUBLE PRECISION NOT NULL,
    housing_median_age INTEGER NOT NULL,
    total_rooms INTEGER NOT NULL,
    total_bedrooms DOUBLE PRECISION,
    population INTEGER NOT NULL,
    households INTEGER NOT NULL,
    median_income DOUBLE PRECISION NOT NULL,
    median_house_value DOUBLE PRECISION NOT NULL,
    ocean_proximity VARCHAR(50) NOT NULL,

    --=========================================
    -- Metadata Columns (Data Governance)
    --=========================================
    ingestion_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    source_file VARCHAR(255),
    batch_id UUID,

    --=========================================
    -- Basic Integrity Constraints
    --=========================================
    CONSTRAINT chk_longitude_range CHECK (longitude >= -180 AND longitude <= 180),

    CONSTRAINT chk_latitude_range CHECK (latitude >= -90 AND latitude <= 90),

    CONSTRAINT chk_population_positive CHECK (population >= 0),

    CONSTRAINT chk_rooms_positive CHECK (total_rooms >= 0),

    CONSTRAINT chk_households_positive CHECK (households >= 0)
    
);

    --=========================================
    -- Indexes for Performance Optimization
    --=========================================

    CREATE INDEX IF NOT EXISTS idx_raw_housing_batch_id ON raw_housing(batch_id);
    CREATE INDEX IF NOT EXISTS idx_raw_housing_ingestion_timestamp ON raw_housing(ingestion_timestamp);
    CREATE INDEX IF NOT EXISTS idx_raw_housing_ocean_proximity ON raw_housing(ocean_proximity);
    