import pydantic

from ..domain import IncidentType

class CreateIncidentRequest(pydantic.BaseModel):
    title: str
    description: str | None
    location: str | None
    incident_type: IncidentType

