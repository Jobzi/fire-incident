import pydantic

from .incident_enum import IncidentType


class Incident(pydantic.BaseModel):
    id: str
    title: str
    description: str | None
    location: str | None
    incident_type: IncidentType
    image: str | None = None
