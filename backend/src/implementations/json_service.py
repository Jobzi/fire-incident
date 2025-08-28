import json
import os
from re import I

from ..domain import Incident, StorageService

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "src", "storage", "incident.json")
os.makedirs(os.path.dirname(UPLOAD_FOLDER), exist_ok=True)

IMAGE_FOLDER = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "src", "storage", "images")
os.makedirs(IMAGE_FOLDER, exist_ok=True)

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
                location=item.get("location"),
                image=item.get("image")
            ) for item in json.load(f)]

    def save(self, data: Incident) -> None:
        local_data = self.read()
        local_data.append(data)
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump([item.model_dump() for item in local_data], f, ensure_ascii=False, indent=2)

    def save_image(self, image_data: bytes, filename: str) -> str:
        image_path = os.path.join(IMAGE_FOLDER, filename)
        with open(image_path, "wb") as f:
            f.write(image_data)
        return image_path
