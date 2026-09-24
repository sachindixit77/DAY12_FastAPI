# Employee Management API

## Project Overview

This project is an Employee Management API developed using FastAPI.

The API is used to create, view, search, update, and delete employee records.

It also includes data validation, error handling, HTTP status codes, and Swagger documentation.

## Technologies Used

* Python
* FastAPI
* Pydantic
* Uvicorn
* Swagger / OpenAPI
* Git and GitHub

## Project Structure

```text
day12-fastapi/
├── main.py
├── models.py
├── requirements.txt
├── README.md
├── API_DOCUMENTATION.md
└── .gitignore
```

## API Endpoints

| Method | Endpoint                          | Description                    |
| ------ | --------------------------------- | ------------------------------ |
| POST   | `/employees`                      | Create a new employee          |
| GET    | `/employees`                      | Get all employees              |
| GET    | `/employees/search?department=IT` | Search employees by department |
| GET    | `/employees/{id}`                 | Get employee by ID             |
| PUT    | `/employees/{id}`                 | Update an employee             |
| DELETE | `/employees/{id}`                 | Delete an employee             |

## Validation

Pydantic is used to validate employee data.

The API checks:

* Name must have at least 2 characters.
* Department must have at least 2 characters.
* Designation must have at least 2 characters.
* Salary must be greater than 0.

Invalid data returns a `422 Unprocessable Entity` response.

## Error Handling

The API uses HTTP exceptions to handle errors.

For example, if an employee ID does not exist, the API returns:

```json
{
  "detail": "Employee not found"
}
```

with a `404 Not Found` status code.

## HTTP Status Codes

* `200 OK` – Request completed successfully.
* `201 Created` – Employee created successfully.
* `404 Not Found` – Employee does not exist.
* `422 Unprocessable Entity` – Validation failed.

## Swagger Documentation

FastAPI automatically provides interactive API documentation using Swagger UI.

After starting the server, open:

```text
http://127.0.0.1:8000/docs
```

Swagger can be used to test all API endpoints directly from the browser.

## How to Run the Project

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Then open Swagger:

```text
http://127.0.0.1:8000/docs
```

## Learning Outcome

In this project, I learned how to:

* Build a FastAPI application.
* Create API routes.
* Use GET, POST, PUT, and DELETE methods.
* Use path parameters.
* Use query parameters.
* Use Pydantic models.
* Validate request data.
* Handle API errors.
* Use HTTP status codes.
* Test APIs using Swagger.
* Document and manage a project using Git and GitHub.
