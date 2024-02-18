from fastapi import FastAPI, APIRouter
from sch_registration import sch_router
from st_registration import st_router
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

origins = [
    "https://jolly-sea-09141a40f.4.azurestaticapps.net",  # Replace with your frontend origin
    # "http://localhost:3000",  # Add more origins if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Your routes go here



app.include_router(sch_router)
app.include_router(st_router)