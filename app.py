import random
import os
import requests
from flask import Flask, render_template, abort, request


from MemeEngine import MemeEngine
from QuoteEngine import Ingestor
app = Flask(__name__)

meme = MemeEngine('./static/')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for quote_file in quote_files:
        Quotes = Ingestor.parse(quote_file)
        for quote in Quotes:
            print(quote)
            quotes.append(quote)

    images_path = "./_data/photos/dog/"

    imgs = os.listdir(images_path)

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    images_path = "./_data/photos/dog/"
    img = random.choice(imgs)
    full_image_path = f'{images_path}{img}'
    quote = random.choice(quotes)
    path = meme.make_meme(full_image_path, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    img_url = request.form['image_url']
    tmp = tmp = f'./tmp/{random.randint(1,1000)}.png'
    r = requests.get(img_url)
    file = open(tmp, 'wb').write(r.content)

    body = request.form['body']
    author = request.form['author']

    path = meme.make_meme(tmp, body, author)
    os.remove(tmp)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
