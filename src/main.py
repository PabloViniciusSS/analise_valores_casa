# src/main.py

import sys
from pathlib import Path

from src.core.logger import logger
from src.core.settings import get_settings
from src.layers.raw.ingestion import ingest_raw_housing

# Import necessário para criar tabelas
from src.core.database import engine
from src.layers.raw.models import Base  # Ajuste conforme seu model RawHousing


def main() -> None:
    """
    Entry point do pipeline.

    Responsável apenas por orquestrar as camadas.
    """

    settings = get_settings()

    logger.info("====================================")
    logger.info("INICIANDO PIPELINE")
    logger.info(f"Ambiente: {settings.ENVIRONMENT}")
    logger.info("====================================")

    try:
        # ======================================
        # Criação das tabelas no banco
        # ======================================
        logger.info("Criando tabelas no banco, se não existirem...")
        Base.metadata.create_all(bind=engine)
        logger.info("Tabelas criadas com sucesso (ou já existiam).")

        # ======================================
        # RAW Stage
        # ======================================
        file_path = Path(settings.RAW_DATA_PATH)

        if not file_path.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

        batch_id = ingest_raw_housing(file_path)

        logger.info(f"RAW concluído com sucesso | Batch ID: {batch_id}")
        logger.info("PIPELINE FINALIZADO COM SUCESSO")

    except Exception as exc:
        logger.exception("Erro durante execução do pipeline.")
        sys.exit(1)


if __name__ == "__main__":
    main()