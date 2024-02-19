from fastapi import APIRouter, HTTPException, Depends
from db import get_db
import pyodbc
from pydantic import BaseModel
import random
import string

class TeacherRegistration(BaseModel):
    SCHOOL_ID: str
    TEACHER_NAME: str
    QUALIFICATION: str
    AADHAR_NO: str
    TEACHER_MOBILE: str
    TEACHER_EMAIL: str
    DOC_ID: str

    D_NO: str
    STREET: str
    AREA: str
    CITY: str
    DISTRICT: str
    STATE: str
    PIN_CODE: str

tea_router = APIRouter()

@tea_router.post("/tregister")
async def register_teacher(teacher: TeacherRegistration, db=Depends(get_db)):
    # Generate TEACHER_ID and PASSWORD
    TEACHER_ID = 't'+teacher.TEACHER_NAME[:2] + teacher.SCHOOL_ID[3:6] + ''.join(random.choices(string.digits, k=4))
    PASSWORD = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

    cursor = db.cursor()

    # Insert into teachers table
    cursor.execute(
        "INSERT INTO teachers (SCHOOL_ID, TEACHER_ID, TEACHER_NAME, QUALIFICATION, AADHAR_NO, TEACHER_MOBILE, TEACHER_EMAIL, DOC_ID, PASSWORD) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
        teacher.SCHOOL_ID, TEACHER_ID, teacher.TEACHER_NAME, teacher.QUALIFICATION, teacher.AADHAR_NO, teacher.TEACHER_MOBILE, teacher.TEACHER_EMAIL, teacher.DOC_ID, PASSWORD
    )

    # Insert into address table
    cursor.execute(
        "INSERT INTO address (ID, MOBILE, D_NO, STREET, AREA, CITY, DISTRICT, STATE, PIN_CODE) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
        TEACHER_ID, teacher.TEACHER_MOBILE, teacher.D_NO, teacher.STREET, teacher.AREA, teacher.CITY, teacher.DISTRICT, teacher.STATE, teacher.PIN_CODE
    )

    db.commit()

    return {"message": "Teacher registration successful"}