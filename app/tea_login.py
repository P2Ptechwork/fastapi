from fastapi import APIRouter, HTTPException, Depends
from db import get_db
import pyodbc
from pydantic import BaseModel

tl_router = APIRouter()

class TeacherLogin(BaseModel):
    teacherId: str
    password: str

@tl_router.post("/teacher_login")
async def teacher_login(teacher: TeacherLogin, db=Depends(get_db)):
    teacherId = teacher.teacherId
    password = teacher.password
    print(teacherId, password)

    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM teachers WHERE TEACHER_ID = '{teacherId}' AND PASSWORD = '{password}'")
    row = cursor.fetchone()

    if row is None:
        raise HTTPException(status_code=400, detail="Invalid teacherId or password")

    return {"message": "Login successful", "schoolId": row.SCHOOL_ID}