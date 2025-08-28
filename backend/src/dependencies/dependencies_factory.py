from ..cases import CreateIncidentUseCase, GetIncidentsUseCase
from .services import storage_service


def create_incident_use_case() -> CreateIncidentUseCase:
    return CreateIncidentUseCase(
        storage_service=storage_service()
    )


def get_incidents_use_case() -> GetIncidentsUseCase:
    return GetIncidentsUseCase(
        storage_service=storage_service()
    )
