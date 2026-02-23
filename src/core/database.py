
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.engine import Engine
from contextlib import contextmanager

from src.core.settings import get_settings

settings = get_settings()

class Base(DeclarativeBase):
    """Base class for SQLAlchemy models."""
    pass

def get_engine() -> Engine:
    return create_engine(
        settings.DATABASE_URL,
        echo=False,
        future=True, # Adicionada vírgula
        pool_pre_ping=True 
    )

engine: Engine = get_engine()

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine, # Adicionada vírgula
    expire_on_commit=False
)

@contextmanager
def get_db_session():
    """
    Context manager para controle transacional.

    Garante:
    - commit automático
    - rollback em caso de erro
    - fechamento da sessão
    """
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()