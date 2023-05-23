from typing import Optional

from pydantic import BaseSettings, EmailStr

import os

from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    """Класс для хранения настроек приложения."""

    app_title: str = (
        'QRKot - Благотворительный фонд поддержки бездомных котиков'
    )
    app_description: str = 'Благотворительный фонд поддержки бездомных котиков'
    database_url: str = os.getenv('DATABASE_URL')
    secret: str = os.getenv('SECRET')
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()
