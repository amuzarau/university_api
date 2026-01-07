University API

A simple yet production‑style University API.

The project demonstrates how to design, build, test, and run a modern full‑stack backend application using FastAPI with a PostgreSQL database, containerized with Docker Compose, and complemented by a lightweight Streamlit frontend.

🎯 Project Goals

The main goals of this project are:

Learn FastAPI fundamentals and REST API design

Connect FastAPI to PostgreSQL using psycopg2

Manage database schema with simple migration scripts

Write automated API tests with pytest

Run the application locally and inside Docker Compose

Build a minimal Streamlit UI as a frontend client

This repository is intended as a learning and demonstration project, following best practices expected in real‑world backend development.

🧰 Tech Stack

Python 3.12

FastAPI – backend REST API

PostgreSQL – relational database

psycopg2 – PostgreSQL driver

Pydantic – data validation and settings management

pytest – automated testing

Docker & Docker Compose – containerization and service orchestration

Streamlit – simple web UI for interacting with the API

📁 Project Structure
university_api/
├── app/
│   ├── main.py              # FastAPI application
│   ├── db.py                # Database connection helper
│   ├── config.py            # Application settings (.env support)
│   ├── models/
│   │   └── student.py       # Pydantic models
│   └── migrations/
│       ├── migrations_create_tables.py
│       ├── migrations_clear_db.py
│       └── migrations_connection.py
│
├── streamlit/
│   └── main.py              # Streamlit frontend
│
├── tests/
│   └── test_main.py         # API tests
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
├── .dockerignore
└── README.md
🏗️ Architecture Overview (Mermaid)
flowchart TD
    U[User / Browser]


    S[Streamlit Frontend]
    A[FastAPI Backend]
    DB[(PostgreSQL Database)]


    ENV[.env]
    CFG[Settings]
    CONN[DB Connection]


    U --> S
    S -->|HTTP requests| A


    A --> CFG
    CFG --> ENV
    A --> CONN
    CONN --> DB


    DB --> A
    A --> S
    S --> U
🔄 Request Flow (Sequence Diagram)
sequenceDiagram
    participant User
    participant Streamlit
    participant FastAPI
    participant PostgreSQL


    User->>Streamlit: Enter student data
    Streamlit->>FastAPI: POST /student
    FastAPI->>PostgreSQL: INSERT student
    PostgreSQL-->>FastAPI: New record
    FastAPI-->>Streamlit: JSON response
    Streamlit-->>User: UI update


    User->>Streamlit: View students
    Streamlit->>FastAPI: GET /students
    FastAPI->>PostgreSQL: SELECT *
    PostgreSQL-->>FastAPI: Rows
    FastAPI-->>Streamlit: JSON list
    Streamlit-->>User: Render list


    User->>Streamlit: Delete student
    Streamlit->>FastAPI: DELETE /student/{id}
    FastAPI->>PostgreSQL: DELETE record
    PostgreSQL-->>FastAPI: OK
    FastAPI-->>Streamlit: Confirmation
    Streamlit-->>User: UI update
🐳 Docker Compose Architecture
flowchart LR
    DC[Docker Compose]


    API[FastAPI Service]
    DB[(PostgreSQL Service)]


    ENV[.env]


    DC --> API
    DC --> DB


    API -->|TCP| DB
    API --> ENV
    DB --> ENV

Docker Compose manages:

FastAPI container (application logic)

PostgreSQL container (persistent database)

Shared environment variables via .env

⚙️ Environment Variables

Create a .env file in the project root:

DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=university_api_db
DATABASE_USER=university_api_user
DATABASE_PASSWORD=university_api_password
▶️ Running the Project Locally
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\Activate.ps1      # Windows PowerShell


pip install -r requirements.txt


python -m app.migrations.migrations_create_tables
uvicorn app.main:app --reload --port 8080

API Docs:

http://localhost:8080/docs

🖥 Streamlit Frontend
streamlit run streamlit/main.py
🧪 Running Tests
pytest
🐳 Running with Docker Compose
docker compose up --build
📌 API Endpoints
Method	Endpoint	Description
GET	/	Root endpoint
GET	/status	Health check
POST	/student/	Create a student
GET	/students/	Get all students
DELETE	/student/{id}	Delete student by ID
