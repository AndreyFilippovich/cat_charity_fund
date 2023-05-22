from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'Название проекта'
    app_description: str = 'Описание проекта'
    database_url: str = 'sqlite+aiosqlite:///./qrkot.db'
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = 'andrejfilippovic8@gmail.com'
    first_superuser_password: Optional[str] = 31523956

    class Config:
        env_file = '.env'


settings = Settings()
