from fastapi import APIRouter, HTTPException, Depends
from db import get_db
import pyodbc
from pydantic import BaseModel
import random
import string

class SchoolRegistration(BaseModel):
    D_NO: str
    STREET: str
    AREA: str
    CITY: str
    DISTRICT: str
    STATE: str
    PIN_CODE: str
    GEO_TAG: str
    SCHOOL_NAME: str
    SYLLABUS_TYPE: str
    ADH_NAME: str
    ADH_MOBILE: str
    ADH_EMAIL: str

sch_router = APIRouter()

@sch_router.post("/schregister")
async def register_school(school: SchoolRegistration):
    # Generate SCHOOL_ID and PASSWORD
    SCHOOL_ID = school.CITY[:3] + school.SCHOOL_NAME[:3] + ''.join(random.choices(string.digits, k=4))
    PASSWORD = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    db =  get_db()
    cursor = db.cursor()

    # Insert into schools table
    cursor.execute(
        "INSERT INTO schools (SCHOOL_ID, SCHOOL_NAME, SYLLABUS_TYPE, ADH_NAME, ADH_MOBILE, ADH_EMAIL, PASSWORD) VALUES (?, ?, ?, ?, ?, ?, ?)",
        SCHOOL_ID, school.SCHOOL_NAME, school.SYLLABUS_TYPE, school.ADH_NAME, school.ADH_MOBILE, school.ADH_EMAIL, PASSWORD
    )

    # Insert into address table
    cursor.execute(
        "INSERT INTO address_final (ID, MOBILE, D_NO, STREET, AREA, CITY, DISTRICT, STATE, PIN_CODE, GEO_TAG) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        SCHOOL_ID, school.ADH_MOBILE, school.D_NO, school.STREET, school.AREA, school.CITY, school.DISTRICT, school.STATE, school.PIN_CODE, school.GEO_TAG
    )

    db.commit()

    return {"SCHOOL_ID": SCHOOL_ID, "PASSWORD": PASSWORD}