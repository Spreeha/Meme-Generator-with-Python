import abc
from abc import ABC, abstractmethod

extensions = {
    "TEXT": ".txt",
    "CSV": ".csv",
    "PDF": ".pdf",
    "DOCX": ".docx",
}


class IngestorInterface(ABC):
    @classmethod
    def can_ingest(cls, file_extension):
        return file_extension in extensions.values()
    
    @abstractmethod
    def parse(cls, path):
        pass