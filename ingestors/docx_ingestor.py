from docx import Document

from models import QuoteModel
from ingestors.ingestor_interface import IngestorInterface

class DocxIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        doc = Document(path)
        quotes_in_doc = []
        for para in doc.paragraphs:
            para.text and quotes_in_doc.append(QuoteModel(*para.text.split(" - ")))
        
        return quotes_in_doc