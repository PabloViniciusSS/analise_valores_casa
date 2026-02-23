import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path

from src.core.settings import get_settings

settings = get_settings()

def setup_logger():
    """
    Configuração centralizadas de logging.
    
    Caracteristicas:
    - Log estruturado
    - Rotação de arquivos
    - Console + File handler
    - Nível configuravel por ambiente
    """

    logger = logging.getLogger("casa_ds_logger")
    logger.setLevel(settings.LOG_LEVEL)

    if logger.handlers:
        return logger  # Evita configuração duplicada
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    
    #==============================
    # Console Handler
    #==============================
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    #==============================
    # File Handler com rotação
    #==============================
    settings.logs_dir.mkdir(parents=True, exist_ok=True)  # Garante que o diretório de logs exista

    file_handler = RotatingFileHandler(
        settings.logs_dir / "app.log",
        maxBytes=5*1024*1024,  # 5 MB
        backupCount=5
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.propagate = False  # Evita propagação para loggers raiz

    return logger

logger = setup_logger()