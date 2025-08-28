import uuid

from ._request import CreateIncidentRequest
from ._response import CreateIncidentResponse
from ..domain.services import StorageService


class CreateIncidentUseCase:
    def __init__(self, storage_service: StorageService) -> None:
        self.storage_service = storage_service

    def __call__(self, req: CreateIncidentRequest) -> CreateIncidentResponse:
        incident_id = str(uuid.uuid4())
        self.storage_service.save({"id": incident_id, **req.model_dump()})
        return CreateIncidentResponse(id=incident_id, message=req.description or "No description provided")
