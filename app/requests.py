import requests
from .models import Quote


api = "http://quotes.stormconsultancy.co.uk/random.json"


def getQuotes():
    random_quote = requests.get(api).json()

    quote = Quote(random_quote.get('author'), random_quote.get('quote'))

    return quote

