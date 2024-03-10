import os

from dotenv import load_dotenv
load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI: str = os.getenv("DATABASE_URL")
    PROD_SECRET_KEY: str = os.getenv("SECRET_KEY")

