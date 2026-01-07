"""
Database migration script for creating tables.
"""

from app.migrations.migrations_connection import get_connection


def create_tables() -> None:
    """
    Create required database tables if they do not exist.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Students (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL
        );
    """)

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    create_tables()
