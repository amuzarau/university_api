import streamlit as st
import requests

# Endpoint URLs
create_student_url = "http://localhost:8080/student/"
delete_student_url = "http://localhost:8080/student/"
get_students_url = "http://localhost:8080/students/"


def create_student(first_name, last_name):
    #  Make a POST request to create a new student
    payload = {"first_name": first_name, "last_name": last_name}
    response = requests.post(create_student_url, json=payload)
    if response.status_code == 200:
        st.success("Student created successfully!")
    else:
        st.error("Failed to create student.")


def delete_student(student_id):
    # Make a DELETE request to delete a student
    delete_url = f"{delete_student_url}{student_id}"
    response = requests.delete(delete_url)
    if response.status_code in (200, 204):
        st.success("Student deleted successfully!")
    else:
        st.error("Failed to delete student. Status code: {response.status_code}")


def get_students():
    # Make a GET request to retrieve all students
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


# Main app
def main():
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
