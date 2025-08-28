import uuid

from ._request import CreateIncidentRequest
from ._response import CreateIncidentResponse
from ..domain import StorageService, Incident


class CreateIncidentUseCase:
    def __init__(self, storage_service: StorageService) -> None:
        self.storage_service = storage_service

    def __call__(self, req: CreateIncidentRequest) -> CreateIncidentResponse:
        incident_id = str(uuid.uuid4())
        if req.image:
            image_url = self.storage_service.save_image(req.image, f"incident_{incident_id}.jpg")
            print(f"Image saved at: {image_url}")

        self.storage_service.save(Incident(id=incident_id, description=req.description, incident_type=req.incident_type, location=req.location, title=req.title))
        return CreateIncidentResponse(id=incident_id, message=req.description or "No description provided")
