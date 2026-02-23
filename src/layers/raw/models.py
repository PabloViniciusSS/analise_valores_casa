import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import (
    String,
    Float,
    Integer,
    BigInteger,
    CheckConstraint,
    Index,
    TIMESTAMP,
    text,
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from src.core.database import Base


class RawHousing(Base):

    __tablename__ = "raw_housing"

    # ===============================
    # Primary Key (BIGSERIAL)
    # ===============================
    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    # ===============================
    # Dataset Columns
    # ===============================
    longitude: Mapped[float] = mapped_column(Float, nullable=False)
    latitude: Mapped[float] = mapped_column(Float, nullable=False)

    housing_median_age: Mapped[int] = mapped_column(Integer, nullable=False)
    total_rooms: Mapped[int] = mapped_column(Integer, nullable=False)
    total_bedrooms: Mapped[Optional[float]] = mapped_column(Float, nullable=True)

    population: Mapped[int] = mapped_column(Integer, nullable=False)
    households: Mapped[int] = mapped_column(Integer, nullable=False)

    median_income: Mapped[float] = mapped_column(Float, nullable=False)
    median_house_value: Mapped[float] = mapped_column(Float, nullable=False)

    ocean_proximity: Mapped[str] = mapped_column(String(50), nullable=False)

    # ===============================
    # Metadata
    # ===============================
    ingestion_timestamp: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    source_file: Mapped[Optional[str]] = mapped_column(String(255))
    batch_id: Mapped[Optional[uuid.UUID]] = mapped_column(UUID(as_uuid=True))

    # ===============================
    # Constraints + Indexes
    # ===============================
    __table_args__ = (

        CheckConstraint("longitude >= -180 AND longitude <= 180", name="chk_longitude_range"),
        CheckConstraint("latitude >= -90 AND latitude <= 90", name="chk_latitude_range"),
        CheckConstraint("population >= 0", name="chk_population_positive"),
        CheckConstraint("total_rooms >= 0", name="chk_rooms_positive"),
        CheckConstraint("households >= 0", name="chk_households_positive"),

        Index("idx_raw_housing_batch_id", "batch_id"),
        Index("idx_raw_housing_ingestion_timestamp", "ingestion_timestamp"),
        Index("idx_raw_housing_ocean_proximity", "ocean_proximity"),
    )