"""
Database connection utility for migration scripts.
"""

import psycopg2
from psycopg2.extensions import connection
from app.config import settings


def get_connection() -> connection:
    """
    Create a direct database connection for migrations.

    Returns:
        psycopg2 database connection.
    """
    return psycopg2.connect(
        host=settings.DATABASE_HOST,
        dbname=settings.DATABASE_NAME,
        user=settings.DATABASE_USER,
        password=settings.DATABASE_PASSWORD,
        port=settings.DATABASE_PORT,
    )
