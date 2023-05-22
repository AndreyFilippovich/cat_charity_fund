from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'Название проекта'
    app_description: str = 'Описание проекта'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = 'admin@admin.com'
    first_superuser_password: Optional[str] = 123456

    class Config:
        env_file = '.env'


settings = Settings()
