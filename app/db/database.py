from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

# Создание подключения к базе данных
engine = create_engine(settings.DATABASE_URL)

# Создание базового класса для моделей
Base = declarative_base()

# Создание сессии
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Функция для получения сессии
def get_db():
    """
    Заглушка
    :return:
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
