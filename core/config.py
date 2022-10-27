from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from fastapi.templating import Jinja2Templates
from pathlib import Path


class Settings(BaseSettings):
    DB_URL: str = 'sqlite+aiosqlite:///./sql_app'
    DBBaseModel = declarative_base()
    TEMPLATES = Jinja2Templates(directory='templates')
    MEDIA = Path('media')
    AUTH_COOKIE_NAME: str = 'eessystem'
    SALTY: str = '3Ysy4y8Q1HB7OHHoxDIQz3j4sFtuVfTrUn6-NvjS9DGV7S2fIwP9DtFhOQltrnUJ68otVNP41rxCHxU6SuB9dw'

    class Config:
        case_sensitive: True


settings: Settings = Settings()