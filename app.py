import os
import random
import shutil

import requests
from flask import Flask, render_template, request

from meme import MemeEngine
from ingestors import Ingestor

# @TODO Import your Ingestor and MemeEngine classes

app = Flask(__name__)

static_dir = "./static"
if os.path.exists(static_dir):
    shutil.rmtree(static_dir)
meme = MemeEngine(static_dir)

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store'
    return response


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable

    quotes = []
    for file in quote_files:
        try:
            quotes.extend(Ingestor.parse(file))
        except ValueError as error:
            print(f"ValueError: {error}")
    # quotes = None

    images_path = "./_data/photos/dog/"
    images = []
    for root, dirs, files in os.walk(images_path):
        images = [os.path.join(root, name) for name in files]
    return quotes, images

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    

    # return quotes, imgs


quotes, images = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(images)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    img = "./temp_image.jpg"
    image_url = request.form.get("image_url")
    img_data = requests.get(image_url, stream=True).content
    with open(img, "wb") as f:
        f.write(img_data)

    body = request.form.get("body", "")
    author = request.form.get("author", "")
    path = meme.make_meme(img, body, author)
    print(path)
    os.remove(img)
    return render_template("meme.html", path=path)


if __name__ == "__main__":
    app.run()
