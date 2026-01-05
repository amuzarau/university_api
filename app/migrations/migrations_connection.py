import psycopg2
from app.config import settings


def get_connection():
    return psycopg2.connect(
        host=settings.DATABASE_HOST,
        dbname=settings.DATABASE_NAME,
        user=settings.DATABASE_USER,
        password=settings.DATABASE_PASSWORD,
        port=settings.DATABASE_PORT,
    )
