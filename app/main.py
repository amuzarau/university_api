"""
Main FastAPI application module.

Defines API endpoints for managing students.
"""

from typing import List, Dict, Any

from fastapi import FastAPI, HTTPException

from app.db import get_db_connection
from app.models.student import StudentCreate, Student


# FastAPI application instance
app = FastAPI(title="University API")


@app.get("/")
def read_root() -> Dict[str, str]:
    """
    Root endpoint for sanity check.

    Returns:
        A simple greeting message.
    """
    return {"Hello": "World"}


@app.get("/status")
async def status() -> Dict[str, str]:
    """
    Health check endpoint.

    Returns:
        Application status message.
    """
    return {"message": "OK"}


@app.post("/student/", response_model=Student)
def create_student(student: StudentCreate) -> Student:
    """
    Create a new student record.

    Args:
        student: StudentCreate object containing first and last name.

    Returns:
        The newly created Student object.

    Raises:
        HTTPException: If database operation fails.
    """
    conn, cursor = get_db_connection()
    try:
        cursor.execute(
            """
            INSERT INTO Students (first_name, last_name)
            VALUES (%s, %s)
            RETURNING *
            """,
            (student.first_name, student.last_name),
        )
        new_student: Dict[str, Any] | None = cursor.fetchone()
        conn.commit()
        cursor.close()
    except Exception as e:
        conn.close()
        raise HTTPException(status_code=500, detail=str(e))

    conn.close()
    if new_student:
        return Student(**new_student)

    raise HTTPException(status_code=400, detail="Error creating student")


@app.get("/students/", response_model=List[Student])
def get_all_students() -> List[Student]:
    """
    Retrieve all students from the database.

    Returns:
        List of Student objects.

    Raises:
        HTTPException: If no students are found or database fails.
    """
    students: List[Student] = []
    conn, cursor = get_db_connection()
    try:
        cursor.execute("SELECT * FROM Students")
        rows: List[Dict[str, Any]] = cursor.fetchall()
        for row in rows:
            students.append(Student(**row))
        cursor.close()
    except Exception as e:
        conn.close()
        raise HTTPException(status_code=500, detail=str(e))

    conn.close()
    if students:
        return students
    raise HTTPException(status_code=400, detail="Student not found")


@app.delete("/student/{student_id}")
def delete_student(student_id: int) -> Dict[str, str]:
    """
    Delete a student by ID.

    Args:
        student_id: ID of the student to delete.

    Returns:
        Confirmation message.
    """
    conn, cursor = get_db_connection()
    try:
        cursor.execute("DELETE FROM Students WHERE id = %s", (student_id,))
        conn.commit()
        cursor.close()
    except Exception as e:
        conn.close()
        raise HTTPException(status_code=500, detail=str(e))

    conn.close()
    return {"message": "Student deleted successfully"}
