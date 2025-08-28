import abc


class StorageService(abc.ABC):
    @abc.abstractmethod
    def save(self, data: dict) -> None:
        pass

    @abc.abstractmethod
    def read(self) -> list[dict]:
        pass
