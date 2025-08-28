import json
import os

from ..domain import Incident, StorageService

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "src", "storage", "incident.json")
os.makedirs(os.path.dirname(UPLOAD_FOLDER), exist_ok=True)

class JSONStorageService(StorageService):
    def __init__(self) -> None:
        self.file_path = UPLOAD_FOLDER

    def read(self) -> list[Incident]:
        with open(self.file_path, "r") as f:
            return [
                Incident(
                id=item["id"],
                title=item["title"],
                description=item.get("description"),
                incident_type=item["incident_type"],
                location=item.get("location")
            ) for item in json.load(f)]

    def save(self, data: Incident) -> None:
        local_data = self.read()
        local_data.append(data)
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump([item.model_dump() for item in local_data], f, ensure_ascii=False, indent=2)
    