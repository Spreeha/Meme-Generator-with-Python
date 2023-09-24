from models import QuoteModel
from ingestors.ingestor_interface import IngestorInterface

class TextIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        file = open(path, "r", encoding="utf-8-sig")
        lines = file.readlines()
        file.close()

        quote_models = []

        for quote in lines:
            quote_parts = quote.rstrip("\n").split(" - ")
            quote_model = QuoteModel(*quote_parts)
            quote_models.append(quote_model)

        return quote_models