from fastapi import Depends, FastAPI

from .cases import CreateIncidentRequest, CreateIncidentResponse, CreateIncidentUseCase
from .dependencies import create_incident_use_case

app = FastAPI()

@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello World"}


@app.post("/api/incidents", response_model=CreateIncidentResponse)
def create_incident(
    req: CreateIncidentRequest,
    use_case: CreateIncidentUseCase = Depends(create_incident_use_case)
) -> CreateIncidentResponse:
    return use_case(req)
