from ingestors import Ingestor

quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
               './_data/DogQuotes/DogQuotesDOCX.docx',
               './_data/DogQuotes/DogQuotesPDF.pdf',
               './_data/DogQuotes/DogQuotesCSV.csv']

for sample_file in quote_files:
    try:
        print(Ingestor.parse(sample_file))
    except ValueError as error:
        print(f"ValueError: {error}")