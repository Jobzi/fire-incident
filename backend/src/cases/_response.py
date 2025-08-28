import pydantic


class CreateIncidentResponse(pydantic.BaseModel):
    id: str
    message: str
