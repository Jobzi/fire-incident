from typing import Optional
from fastapi import Depends, FastAPI, Form, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .cases import (
    CreateIncidentRequest,
    CreateIncidentResponse,
    CreateIncidentUseCase,
    GetIncidentsResponse,
    GetIncidentsUseCase
)
from .domain import IncidentType
from .dependencies import create_incident_use_case, get_incidents_use_case

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello World"}


@app.post("/api/incidents", response_model=CreateIncidentResponse)
def create_incident(
    title: str = Form(...),
    description: str = Form(None),
    location: str = Form(None),
    incident_type: IncidentType = Form(...),
    image: Optional[UploadFile] = File(None),
    use_case: CreateIncidentUseCase = Depends(create_incident_use_case)
) -> CreateIncidentResponse:
    if image:
        image_data = image.file.read()
    req = CreateIncidentRequest(
        title=title,
        description=description,
        location=location,
        incident_type=incident_type,
        image=image_data
    )
    return use_case(req)

@app.get("/api/incidents", response_model=GetIncidentsResponse)
def get_incidents(
    use_case: GetIncidentsUseCase = Depends(get_incidents_use_case)
) -> GetIncidentsResponse:
    return use_case()

app.mount("/uploads", StaticFiles(directory="src/storage/images"), name="uploads")
