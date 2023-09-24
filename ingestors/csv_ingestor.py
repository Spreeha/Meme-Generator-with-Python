import pandas as pd
from models import QuoteModel
from ingestors.ingestor_interface import IngestorInterface

class CSVIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        csv = pd.read_csv(path)
        quote_models = []
        for index, row in csv.iterrows():
            quote_model = QuoteModel(**row)
            quote_models.append(quote_model)

        return quote_models