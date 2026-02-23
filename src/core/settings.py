from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from pydantic import Field
from pathlib import Path

class Settings(BaseSettings):
    # Database Settings
    DB_USER: str = Field(..., env='DB_USER')
    DB_PASSWORD: str = Field(..., env='DB_PASSWORD')
    DB_HOST: str = Field("localhost", env='DB_HOST') # Default para rodar local
    DB_PORT: int = Field(5432, env='DB_PORT')
    DB_NAME: str = Field(..., env='DB_NAME')
    DATABASE_URL: str = Field(..., env='DATABASE_URL')

    # Project Settings
    PROJECT_NAME: str = "California Housing Analysis"
    ENVIRONMENT: str = Field("development", env="ENVIRONMENT")
    LOG_LEVEL: str = Field("INFO", env="LOG_LEVEL")

    # Project Paths
    base_dir: Path = Path(__file__).resolve().parent.parent
    data_dir: Path = base_dir / "data"
    models_dir: Path = base_dir / "models"
    logs_dir: Path = base_dir / "logs"

    # ML Hyperparameters
    RANDOM_STATE: int = 42
    TEST_SIZE: float = 0.2
    RAW_DATA_PATH: str = "data/raw/housing.csv"

    # Pydantic Configuration (V2)
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding='utf-8',
        extra="ignore",
        case_sensitive=False
    )

@lru_cache()
def get_settings() -> Settings:
    return Settings()