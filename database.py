from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL para o banco de dados SQLite local
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# Cria a engine do SQLAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    # O connect_args é necessário apenas para SQLite, 
    # pois permite múltiplas threads para a mesma conexão.
)

# Cria a SessionLocal para gerenciar o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para definir os modelos (tabelas)
Base = declarative_base()