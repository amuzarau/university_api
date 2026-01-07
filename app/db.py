"""
Database connection utilities.

Provides a helper function to establish and retry a PostgreSQL connection.
"""

import psycopg2
from typing import Tuple
from psycopg2.extensions import connection, cursor
from psycopg2.extras import RealDictCursor
import time

from app.config import settings


def get_db_connection() -> Tuple[connection, cursor]:
    """
    Establish a PostgreSQL database connection.

    Retries indefinitely until the connection is successful.
    Returns both the connection and a cursor configured to return
    rows as dictionaries.

    Returns:
        Tuple containing:
        - psycopg2 connection object
        - psycopg2 cursor object
    """
    while True:
        try:
            conn = psycopg2.connect(
                host=settings.DATABASE_HOST,
                database=settings.DATABASE_NAME,
                user=settings.DATABASE_USER,
                password=settings.DATABASE_PASSWORD,
                cursor_factory=RealDictCursor,
            )
            cur: cursor = conn.cursor()
            print("Connection Successful")
            return conn, cur
        except Exception as error:
            # Retry connection after a short delay if the database is unavailable
            print("Connection Failed")
            print("Error: ", error)
            time.sleep(2)
