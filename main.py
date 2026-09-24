from fastapi import FastAPI, HTTPException, status
from models import EmployeeCreate, EmployeeResponse

app = FastAPI(
    title="Employee Management API",
    description="A simple FastAPI application for managing employees",
    version="1.0.0"
)

# Temporary employee storage
employees = []


# 1. Create Employee
@app.post(
    "/employees",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED
)
def create_employee(employee: EmployeeCreate):

    new_employee = {
        "id": len(employees) + 1,
        **employee.model_dump()
    }

    employees.append(new_employee)

    return new_employee


# 2. Get All Employees
@app.get(
    "/employees",
    response_model=list[EmployeeResponse]
)
def get_employees():
    return employees


# 3. Search Employees by Department
# IMPORTANT: This route must come before /employees/{id}
@app.get(
    "/employees/search",
    response_model=list[EmployeeResponse]
)
def search_employees(department: str):

    result = [
        employee
        for employee in employees
        if employee["department"].lower() == department.lower()
    ]

    return result


# 4. Get Employee by ID
@app.get(
    "/employees/{id}",
    response_model=EmployeeResponse
)
def get_employee(id: int):

    for employee in employees:
        if employee["id"] == id:
            return employee

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Employee not found"
    )


# 5. Update Employee
@app.put(
    "/employees/{id}",
    response_model=EmployeeResponse
)
def update_employee(id: int, employee: EmployeeCreate):

    for existing_employee in employees:

        if existing_employee["id"] == id:

            existing_employee.update(
                employee.model_dump()
            )

            return existing_employee

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Employee not found"
    )


# 6. Delete Employee
@app.delete("/employees/{id}")
def delete_employee(id: int):

    for index, employee in enumerate(employees):

        if employee["id"] == id:

            employees.pop(index)

            return {
                "message": "Employee deleted successfully"
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Employee not found"
    )