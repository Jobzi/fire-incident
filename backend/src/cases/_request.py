from email.mime import image
import pydantic

from ..domain import IncidentType

class CreateIncidentRequest(pydantic.BaseModel):
    title: str
    description: str | None = None
    location: str | None = None
    incident_type: IncidentType
    image: bytes | None = None

