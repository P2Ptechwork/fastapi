from fastapi import APIRouter, HTTPException, Depends
from db import get_db1
import pyodbc
from pydantic import BaseModel

class SchoolLogin(BaseModel):
    schoolId: str
    password: str

schl_router = APIRouter()

@schl_router.post("/sch_login")
async def school_login(school: SchoolLogin, db=Depends(get_db1)):
    schoolId = school.schoolId
    password = school.password

    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM schools WHERE SCHOOL_ID = '{schoolId}' AND PASSWORD = '{password}'")
    row = cursor.fetchone()

    if row is None:
        raise HTTPException(status_code=400, detail="Invalid schoolId or password")

    return {"message": "Login successful"}