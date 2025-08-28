from ..domain.services import StorageService
from ..implementations import JSONStorageService


def storage_service() -> StorageService:
    return JSONStorageService()
