Project Setup

This guide explains how to set up the server, configure the environment, and run migrations using Alembic.

Prerequisites

Ensure the following are installed on your machine:
- Python 3.8 or higher
- pip (Python package manager)
- MySQL
- Virtual environment tool

Steps to Set Up the Server

1. Clone the Repository

2. Set Up a Virtual Environment

```sh
	python -m venv .venv
	source .venv/bin/activate
```
3. Install Dependencies

```sh
	pip install -r requirements.txt
```
4. Configure Environment Variables

Create a .env file in the root directory and add the following variables:

```ini
	PORT=8000
	DATABASE_URL=mysql+mysqlconnector://<username>:<password>@<host>:<port>/<database_name>
	JWT_SECRET=your_secret_key
	RAPID_API_KEY=your_rapidapi_key
```

5. Apply Migrations
```sh
	alembic upgrade head
```

6. Run the Server

Start the FastAPI server:

```sh
	fastapi dev app/main.py
```

The server will be available at: http://127.0.0.1:8000

7. Import the postman collection to test out the API