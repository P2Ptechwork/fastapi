
from pydantic import BaseModel
import random
import string

from fastapi import APIRouter

st_router = APIRouter()

from db import get_db

class Student(BaseModel):
    SCHOOL_ID: str
    STUDENT_NAME: str
    GRADE: str
    SECTION: str
    AADHAR_NO: str
    GUARDIAN_NAME: str
    RELATION: str
    GUARDIAN_MOBILE: str
    GUARDIAN_EMAIL: str
    DOC_ID: str
    D_NO: str
    STREET: str
    AREA: str
    CITY: str
    DISTRICT: str
    STATE: str
    PIN_CODE: str


@st_router.post("/st_register")
async def register_student_endpoint(student: Student):
    data = student.dict()
    cnxn = get_db()
    cursor = cnxn.cursor()
    # Generate student ID
    random_int = str(random.randint(100, 999))
    school_id = data['SCHOOL_ID']
    grade_str = data['GRADE'].zfill(2)
    student_id = "S" + school_id[:2] + school_id[3:5] + grade_str + random_int

# Assuming school_id and grade are defined


# Format grade to be two digits



# Construct student_id

    # Generate a random password
    password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))

    # Insert into students table
    students_query = f"""
    INSERT INTO students (SCHOOL_ID, STUDENT_ID, STUDENT_NAME, GRADE, SECTION, AADHAR_NO, GUARDIAN_NAME, RELATION, GUARDIAN_MOBILE, GUARDIAN_EMAIL, DOC_ID, PASSWORD)
    VALUES ('{school_id}', '{student_id}', '{data['STUDENT_NAME']}', '{data['GRADE']}', '{data['SECTION']}', '{data['AADHAR_NO']}', '{data['GUARDIAN_NAME']}', '{data['RELATION']}', '{data['GUARDIAN_MOBILE']}', '{data['GUARDIAN_EMAIL']}', '{data['DOC_ID']}', '{password}')
    """
    cursor.execute(students_query)

    # Insert into address table
    address_query = f"""
    INSERT INTO address (ID, MOBILE, D_NO, STREET, AREA, CITY, DISTRICT, STATE, PIN_CODE, GEO_TAG)
    VALUES ('{student_id}', '{data['GUARDIAN_MOBILE']}', '{data['D_NO']}', '{data['STREET']}', '{data['AREA']}', '{data['CITY']}', '{data['DISTRICT']}', '{data['STATE']}', '{data['PIN_CODE']}', '')
    """
    cursor.execute(address_query)

    cnxn.commit()

    return {"student_id": student_id, "password": password}