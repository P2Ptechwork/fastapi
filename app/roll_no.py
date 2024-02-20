from fastapi import APIRouter, HTTPException, Depends
from db import get_db
import pyodbc
from pydantic import BaseModel


class RollNumberDetails(BaseModel):
    schoolId: str
    grade: str
    section: str

rl_router = APIRouter()



@rl_router.post("/rlno")
async def generate_roll_numbers(details: RollNumberDetails, db=Depends(get_db)):
    cursor = db.cursor()

    # Add R_NO column if it doesn't exist
    cursor.execute("ALTER TABLE students ADD R_NO int")

    # Get the students with the same school_id, grade, and section
    cursor.execute("SELECT STUDENT_ID FROM students WHERE SCHOOL_ID = ? AND GRADE = ? AND SECTION = ?", (details.schoolId, details.grade, details.section))
    students = cursor.fetchall()

    # Generate and update roll numbers for these students
    for i, student in enumerate(students, start=1):
        cursor.execute("UPDATE students SET R_NO = ? WHERE STUDENT_ID = ? AND R_NO IS NULL", (i, student.STUDENT_ID))

    # Commit the changes
    db.commit()

    return {"message": "Roll numbers generated successfully"}