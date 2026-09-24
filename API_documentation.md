# Employee Management API Documentation

## 1. Introduction

The Employee Management API is a backend application built using FastAPI.

It provides APIs for managing employee information.

The API supports creating, viewing, searching, updating, and deleting employees.

## 2. Base URL

```text
http://127.0.0.1:8000
```

## 3. API Endpoints

| Method | Endpoint                          | Purpose                        |
| ------ | --------------------------------- | ------------------------------ |
| POST   | `/employees`                      | Create an employee             |
| GET    | `/employees`                      | Get all employees              |
| GET    | `/employees/search?department=IT` | Search employees by department |
| GET    | `/employees/{id}`                 | Get employee by ID             |
| PUT    | `/employees/{id}`                 | Update employee                |
| DELETE | `/employees/{id}`                 | Delete employee                |

## 4. POST /employees

Creates a new employee.

### Request Body

```json
{
  "name": "Rahul Sharma",
  "department": "IT",
  "designation": "Software Engineer",
  "salary": 45000
}
```

### Success Response

**Status Code: 201 Created**

```json
{
  "id": 1,
  "name": "Rahul Sharma",
  "department": "IT",
  "designation": "Software Engineer",
  "salary": 45000
}
```

## 5. GET /employees

Returns all employees.

### Success Response

**Status Code: 200 OK**

```json
[
  {
    "id": 1,
    "name": "Rahul Sharma",
    "department": "IT",
    "designation": "Software Engineer",
    "salary": 45000
  }
]
```

## 6. GET /employees/search

Searches employees using the department query parameter.

### Example

```text
/employees/search?department=IT
```

### Query Parameter

```text
department
```

### Success Response

**Status Code: 200 OK**

The API returns the employees belonging to the requested department.

## 7. GET /employees/{id}

Returns one employee using the employee ID.

### Example

```text
/employees/1
```

### Success Response

**Status Code: 200 OK**

If the employee does not exist:

**Status Code: 404 Not Found**

```json
{
  "detail": "Employee not found"
}
```

## 8. PUT /employees/{id}

Updates an existing employee.

### Example

```text
/employees/1
```

### Request Body

```json
{
  "name": "Rahul Sharma",
  "department": "IT",
  "designation": "Senior Software Engineer",
  "salary": 60000
}
```

### Success Response

**Status Code: 200 OK**

The updated employee information is returned.

## 9. DELETE /employees/{id}

Deletes an employee using the employee ID.

### Example

```text
/employees/1
```

### Success Response

**Status Code: 200 OK**

```json
{
  "message": "Employee deleted successfully"
}
```

If the employee does not exist:

**Status Code: 404 Not Found**

```json
{
  "detail": "Employee not found"
}
```

## 10. Validation

The API uses Pydantic for request validation.

For example:

* Name must contain at least 2 characters.
* Department must contain at least 2 characters.
* Designation must contain at least 2 characters.
* Salary must be greater than 0.

### Invalid Request Example

```json
{
  "name": "A",
  "department": "IT",
  "designation": "Developer",
  "salary": -5000
}
```

This request returns:

**422 Unprocessable Entity**

## 11. Error Handling

The API uses `HTTPException` to handle errors.

When an employee is not found, the API returns:

```json
{
  "detail": "Employee not found"
}
```

with status code `404`.

## 12. HTTP Status Codes

| Status Code | Meaning            |
| ----------- | ------------------ |
| 200         | Request successful |
| 201         | Employee created   |
| 404         | Employee not found |
| 422         | Validation error   |

## 13. Swagger / OpenAPI

FastAPI automatically generates interactive API documentation.

Swagger URL:

```text
http://127.0.0.1:8000/docs
```

Using Swagger, we can:

* View all API endpoints.
* Enter request data.
* Execute API requests.
* View response data.
* Check status codes.
* Test validation and errors.

## 14. Conclusion

This project helped me understand how a backend API works using FastAPI.

I learned about API routes, HTTP methods, path parameters, query parameters, Pydantic validation, error handling, status codes, Swagger documentation, and GitHub.
