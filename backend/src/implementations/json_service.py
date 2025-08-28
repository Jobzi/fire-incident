import json
import os

from ..domain.services import StorageService

UPLOAD_FOLDER = "backend/src/storage/incident.json"
os.makedirs(os.path.dirname(UPLOAD_FOLDER), exist_ok=True)

class JSONStorageService(StorageService):
    def __init__(self) -> None:
        self.file_path = UPLOAD_FOLDER

    def read(self) -> list[dict]:
        with open(self.file_path, "r") as f:
            return json.load(f)

    def save(self, data: dict) -> None:
        local_data = self.read()
        local_data.append(data)
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(local_data, f, ensure_ascii=False, indent=2)
