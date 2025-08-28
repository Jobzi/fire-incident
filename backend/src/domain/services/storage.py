import abc

from ..incident import Incident


class StorageService(abc.ABC):
    @abc.abstractmethod
    def save(self, data: Incident) -> None:
        pass

    @abc.abstractmethod
    def read(self) -> list[Incident]:
        pass
