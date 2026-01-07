"""
Streamlit frontend application for the University API.

Provides a simple web interface to create, list, and delete students
via HTTP requests to the FastAPI backend.
"""

from typing import List, Dict, Any

import streamlit as st
import requests

# =========================
# API ENDPOINT CONFIGURATION
# =========================

# Base API endpoints used by the Streamlit UI
create_student_url = "http://localhost:8080/student/"
delete_student_url = "http://localhost:8080/student/"
get_students_url = "http://localhost:8080/students/"

# =========================
# API COMMUNICATION HELPERS
# =========================


def create_student(first_name: str, last_name: str) -> None:
    """
    Create a new student via the backend API by making a POST request.

    Args:
        first_name: Student first name.
        last_name: Student last name.
    """
    payload = {"first_name": first_name, "last_name": last_name}
    response = requests.post(create_student_url, json=payload)
    if response.status_code == 200:
        st.success("Student created successfully!")
    else:
        st.error("Failed to create student.")


def delete_student(student_id: int) -> None:
    """
    Delete a student by ID via the backend API by making a DELETE request.

    Args:
        student_id: ID of the student to delete.
    """

    delete_url = f"{delete_student_url}{student_id}"
    response = requests.delete(delete_url)
    if response.status_code in (200, 204):
        st.success("Student deleted successfully!")
    else:
        st.error("Failed to delete student. Status code: {response.status_code}")


def get_students() -> None:
    """
    Retrieve and display all students from the backend API by making a GET request.
    """
    response = requests.get(get_students_url)
    if response.status_code == 200:
        students = response.json()
        st.write("List of Students:")
        for student in students:
            st.write(
                f"- {student['id']}: {student['first_name']} {student['last_name']}"
            )
    else:
        st.error("Failed to retrieve students.")


# =========================
# STREAMLIT APPLICATION UI
# =========================


# Main app
def main():
    """
    Main Streamlit application entry point.
    """
    st.title("University API")

    # Input fields for first name and last name
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")

    # Submit button
    if st.button("Submit"):
        create_student(first_name, last_name)

    # Delete button
    student_id = st.text_input("Student ID to Delete")
    if st.button("Delete"):
        delete_student(student_id)

    # Display list of students
    get_students()


if __name__ == "__main__":
    main()
