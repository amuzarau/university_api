"""
Utility script for clearing database tables.
"""

from app.migrations.migrations_connection import get_connection


def clear_db() -> None:
    """
    Drop student-related tables from the database.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS students;")

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    clear_db()
