from ..domain import StorageService
from ._response import GetIncidentsResponse


class GetIncidentsUseCase:
    def __init__(self, storage_service: StorageService) -> None:
        self.storage_service = storage_service

    def __call__(self) -> GetIncidentsResponse:
        incidents = self.storage_service.read()
        sorted_incidents = incidents[::-1]
        return GetIncidentsResponse(incidents=sorted_incidents)
