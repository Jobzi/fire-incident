from ._request import CreateIncidentRequest
from ._response import CreateIncidentResponse


class CreateIncidentUseCase:
    def __init__(self) -> None:
        pass

    def __call__(self, req: CreateIncidentRequest) -> CreateIncidentResponse:
        return CreateIncidentResponse(id="1", message=req.description or "No description provided")
