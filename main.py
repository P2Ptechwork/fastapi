from fastapi import FastAPI, APIRouter
from sch_registration import sch_router
from st_registration import st_router
from sch_login import schl_router
from tea_registration import tea_router
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(docs_url="/docs")
@app.get("/")
def read_root():
    return {"Hello": "World"}
origins = [
    "https://jolly-sea-09141a40f.4.azurestaticapps.net",
      "http://localhost:3000"  # Replace with your frontend origin
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
app.include_router(schl_router)
app.include_router(tea_router)