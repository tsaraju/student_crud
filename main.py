from itertools import count

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, EmailStr, Field

app = FastAPI(title="Student Management API")

# In-memory storage; data is cleared when the app stops.
students: dict[int, "Student"] = {}
next_id = count(1)


class StudentInput(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    age: int = Field(ge=1, le=120)
    course: str | None = Field(default=None, max_length=100)


class Student(StudentInput):
    id: int


@app.post(
    "/students",
    response_model=Student,
    status_code=status.HTTP_201_CREATED,
)
def create_student(student_data: StudentInput):
    student_id = next(next_id)
    student = Student(id=student_id, **student_data.model_dump())
    students[student_id] = student
    return student


@app.get("/students", response_model=list[Student])
def get_students():
    return list(students.values())


@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    student = students.get(student_id)

    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    return student


@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, student_data: StudentInput):
    if student_id not in students:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    updated_student = Student(id=student_id, **student_data.model_dump())
    students[student_id] = updated_student
    return updated_student


@app.delete(
    "/students/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    del students[student_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)