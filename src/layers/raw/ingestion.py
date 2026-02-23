
import csv
import uuid
from pathlib import Path
from typing import Iterable

from src.core.database import get_db_session
from src.core.logger import logger
from src.layers.raw.contract import RawHousingContract
from src.layers.raw.models import RawHousing

def read_csv(file_path: Path) -> Iterable[dict]:
    """
    Lê o CSV e retorna cada linha como dicionário.
    Não realiza neenhuma transformação.
    """
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            yield row

def ingest_raw_housing(file_path: Path) -> uuid.UUID:
    """
    Executa a ingestão da camada RAW.

    Fluxo:
    1. Gera batch_id
    2. Lê CSV
    3. Valida via Contract
    4. Persiste via ORM
    5. Commit transacional

    Retorna o batch_id da execução.
    """

    logger.info("Iniciando ingestão RAW.")
    batch_id = uuid.uuid4()

    total_rows = 0

    with get_db_session() as session:
        for row in read_csv(file_path):

            # ==================================================
            # Validação estrutural via Contract
            # ==================================================
            contract_obj = RawHousingContract(**row)

            # ==================================================
            # Conversão Contract → ORM
            # ==================================================
            orm_obj = RawHousing(
                **contract_obj.model_dump(),
                source_file=str(file_path.name),
                batch_id=batch_id,
            )

            session.add(orm_obj)
            total_rows += 1

    logger.info(
        f"Ingestão RAW finalizada. "
        f"Batch ID: {batch_id} | Registros inseridos: {total_rows}"
    )

    return batch_id