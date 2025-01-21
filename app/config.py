import os

class Settings:
    """
    Настройки подключения к БД postgresql
    """
    HOST: str = os.getenv("HOST", "0.0.0.0")  # Используйте 0.0.0.0 для доступа извне
    PORT: int = int(os.getenv("PORT", "8000"))
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://user:password@db/incentive_motivation"
    )

settings = Settings()
