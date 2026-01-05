from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Dict, List

app = FastAPI(title="Student Grade Book System")

class StudentCreate(BaseModel):
    student_id: int
    name: str
    marks: Dict[str, int]

class StudentUpdate(BaseModel):
    marks: Dict[str, int]


class StudentService:
    def __init__(self):
        self.students: List[Dict] = []

    def add_student(self, student: StudentCreate):
        for s in self.students:
            if s["student_id"] == student.student_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Student already exists"
                )
        self.students.append(student.dict())
        return student

    def get_student_by_name(self, name: str):
        for s in self.students:
            if s["name"].lower() == name.lower():
                return s
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    def update_marks(self, student_id: int, marks: Dict[str, int]):
        for s in self.students:
            if s["student_id"] == student_id:
                s["marks"].update(marks)
                return s
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    def delete_student(self, student_id: int):
        for s in self.students:
            if s["student_id"] == student_id:
                self.students.remove(s)
                return
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    def class_average(self):
        if not self.students:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No students available"
            )

        total_marks = 0
        total_subjects = 0

        for s in self.students:
            for mark in s["marks"].values():
                total_marks += mark
                total_subjects += 1

        return total_marks / total_subjects

    def top_students(self):
        if not self.students:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No students available"
            )

        averages = []
        for s in self.students:
            avg = sum(s["marks"].values()) / len(s["marks"])
            averages.append((s, avg))

        max_avg = max(avg for _, avg in averages)
        top_students = [s for s, avg in averages if avg == max_avg]

        return top_students


student_service = StudentService()


@app.post("/students", status_code=status.HTTP_201_CREATED)
def add_student(student: StudentCreate):
    return student_service.add_student(student)


@app.get("/students/name/{name}")
def get_student(name: str):
    return student_service.get_student_by_name(name)


@app.put("/students/{student_id}")
def update_student(student_id: int, update: StudentUpdate):
    return student_service.update_marks(student_id, update.marks)


@app.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int):
    student_service.delete_student(student_id)


@app.get("/students/average")
def get_class_average():
    return {"class_average": student_service.class_average()}


@app.get("/students/top")
def get_top_students():
    return student_service.top_students()
