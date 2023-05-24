from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    """Класс для хранения настроек приложения."""

    app_title: str = (
        'QRKot - Благотворительный фонд поддержки бездомных котиков'
    )
    app_description: str = 'Благотворительный фонд поддержки бездомных котиков'
    database_url: str = 'sqlite+aiosqlite:///./cat_charity.db'
    secret: str = 'shd'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()
