from fastapi import APIRouter, HTTPException, Depends
from db import get_db1
import pyodbc
from pydantic import BaseModel

class student_details(BaseModel):
    schoolId: str
    grade: str
    section: str

std_router = APIRouter()



@std_router.post("/stdetails")
async def get_student_details(details: student_details, db=Depends(get_db1)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM students WHERE SCHOOL_ID = ? AND GRADE = ? AND SECTION = ?", (details.schoolId, details.grade, details.section))
    students_table = cursor.fetchall()
    print(students_table)
    students_table = [dict(zip(["SCHOOL_ID","STUDENT_ID", "STUDENT_NAME", "GRADE", "SECTION","","","","","","", "PASSWORD","R_NO"], student)) for student in students_table]
    print(students_table)
    return {"students": students_table}