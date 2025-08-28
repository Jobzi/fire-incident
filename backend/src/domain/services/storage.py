import abc

from ..incident import Incident


class StorageService(abc.ABC):
    @abc.abstractmethod
    def save(self, data: Incident) -> None:
        pass

    @abc.abstractmethod
    def read(self) -> list[Incident]:
        pass

    @abc.abstractmethod
    def save_image(self, image_data: bytes, filename: str) -> str:
        pass
