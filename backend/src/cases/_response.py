import pydantic

from ..domain import Incident


class CreateIncidentResponse(pydantic.BaseModel):
    id: str
    message: str

class GetIncidentsResponse(pydantic.BaseModel):
    incidents: list[Incident]
