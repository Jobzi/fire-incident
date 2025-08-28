import uuid

from ._request import CreateIncidentRequest
from ._response import CreateIncidentResponse
from ..domain import StorageService, Incident


class CreateIncidentUseCase:
    def __init__(self, storage_service: StorageService) -> None:
        self.storage_service = storage_service

    def __call__(self, req: CreateIncidentRequest) -> CreateIncidentResponse:
        incident_id = str(uuid.uuid4())
        image_name = None
        if req.image:
            image_name = f"incident_{incident_id}.jpg"
            self.storage_service.save_image(req.image, image_name)

        self.storage_service.save(Incident(id=incident_id, description=req.description, incident_type=req.incident_type, location=req.location, title=req.title, image=image_name))
        return CreateIncidentResponse(id=incident_id, message=req.description or "No description provided")
