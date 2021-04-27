from abc import ABC, abstractmethod


class IngestorInterface(ABC):
    files = []

    @classmethod
    def can_ingest(cls, path):
        file_format = path.split('.')[-1]
        return file_format in cls.files

    @classmethod
    @abstractmethod
    def parse(cls, path):
        pass
