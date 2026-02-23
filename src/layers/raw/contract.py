from typing import Optional
from pydantic import BaseModel, Field, field_validator


class RawHousingContract(BaseModel):
    """
    Contract da camada RAW.

    Apenas valida estrutura e tipos.
    Não realiza limpeza ou transformação.
    """

    longitude: float = Field(..., ge=-180, le=180)
    latitude: float = Field(..., ge=-90, le=90)

    housing_median_age: int = Field(..., ge=0)
    total_rooms: int = Field(..., ge=0)
    total_bedrooms: Optional[float]

    population: int = Field(..., ge=0)
    households: int = Field(..., ge=0)

    median_income: float
    median_house_value: float

    ocean_proximity: str

    # 🔹 Coerção mínima estrutural
    @field_validator("*", mode="before")
    @classmethod
    def empty_string_to_none(cls, v):
        if v == "":
            return None
        return v

    class Config:
        extra = "forbid"
        validate_assignment = False