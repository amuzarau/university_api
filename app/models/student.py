"""
Pydantic models for student data validation.
"""

from pydantic import BaseModel


class StudentCreate(BaseModel):
    """
    Schema for creating a student.
    """

    first_name: str
    last_name: str


class Student(StudentCreate):
    """
    Schema representing a student record returned from the API.
    """

    id: int
