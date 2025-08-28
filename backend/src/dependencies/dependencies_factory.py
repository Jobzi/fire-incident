from ..cases import CreateIncidentUseCase
from .services import storage_service


def create_incident_use_case() -> CreateIncidentUseCase:
    return CreateIncidentUseCase(
        storage_service=storage_service()
    )
