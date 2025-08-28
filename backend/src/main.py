from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .cases import (
    CreateIncidentRequest,
    CreateIncidentResponse,
    CreateIncidentUseCase,
    GetIncidentsResponse,
    GetIncidentsUseCase
)
from .dependencies import create_incident_use_case, get_incidents_use_case

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello World"}


@app.post("/api/incidents", response_model=CreateIncidentResponse)
def create_incident(
    req: CreateIncidentRequest,
    use_case: CreateIncidentUseCase = Depends(create_incident_use_case)
) -> CreateIncidentResponse:
    return use_case(req)

@app.get("/api/incidents", response_model=GetIncidentsResponse)
def get_incidents(
    use_case: GetIncidentsUseCase = Depends(get_incidents_use_case)
) -> GetIncidentsResponse:
    return use_case()
