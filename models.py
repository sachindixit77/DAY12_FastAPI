from pydantic import BaseModel, Field


class EmployeeCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    department: str = Field(min_length=2, max_length=50)
    designation: str = Field(min_length=2, max_length=50)
    salary: float = Field(gt=0)


class EmployeeResponse(BaseModel):
    id: int
    name: str
    department: str
    designation: str
    salary: float