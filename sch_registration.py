

from pydantic import BaseModel

import random
import string
from db import get_db


# Define FastAPI instance
from fastapi import APIRouter
sch_router = APIRouter()

# Database connection parameters


# Define Pydantic model for School
class School(BaseModel):
    name: str
    head_name: str
    address: str
    head_email: str
    head_mobile: str

# Generate school ID
def generate_school_id(name):
    prefix = name[:3].upper()  # First 3 letters of school name
    suffix = ''.join(random.choices(string.digits, k=4))  # Random 4-digit number
    return f'LOC{prefix}{suffix}'


@sch_router.post("/schools/")
async def create_school(school: School):
    school_id = generate_school_id(school.name)
    cnxn = get_db()
    cursor = cnxn.cursor()
    cursor.execute("INSERT INTO schools (school_id, name, head_name, address, head_email, head_mobile) VALUES (?, ?, ?, ?, ?, ?)",
                   (school_id, school.name, school.head_name, school.address, school.head_email, school.head_mobile))
    cnxn.commit()

    create_database_query = f"CREATE DATABASE {school.name};"
    cursor.execute(create_database_query)
    cnxn.commit()
    
    return {"school_id": school_id, **school.dict()}
