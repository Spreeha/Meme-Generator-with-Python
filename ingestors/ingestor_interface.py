extensions = {
    "TEXT": ".txt",
    "CSV": ".csv",
    "PDF": ".pdf",
    "DOCX": ".docx",
}


class IngestorInterface:
    @classmethod
    def can_ingest(cls, file_extension):
        return file_extension in extensions.values()
    
    @classmethod
    def parse(cls, path):
        pass