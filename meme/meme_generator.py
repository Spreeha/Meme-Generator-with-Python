import os
import random

from ingestors import Ingestor
from models import QuoteModel
from meme.meme_engine import MemeEngine

def generate_meme(path=None, body=None, author=None):
    """ Generate a meme based on path, quote and author """
    if path is None:
        images_dir = "./_data/photos/dog/"
        images = []
        for root, dirs, files in os.walk(images_dir):
            for name in files:
                file_path = os.path.join(root, name)
                images.append(file_path)

        img_path = random.choice(images)

    else:
        img_path = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    
    meme = MemeEngine('./tmp')
    path = meme.make_meme(img_path, quote.body, quote.author)
    return path