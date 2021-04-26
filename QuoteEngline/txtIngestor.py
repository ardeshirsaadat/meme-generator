from ingestorInterface import IngestorInterface
from quotemodel import QuoteModel


class TXTIngestor(IngestorInterface):
    files = ['txt']

    @classmethod
    def parse(cls, path):
        quotes = []
        if cls.can_ingest(path):
            r = open(path, 'r')
            for line in r.readlines():
                line = line.strip('\n\r').strip()
                line = line.split('-')
                if len(line) > 1:
                    quote = QuoteModel(line[0], line[1])
                    quotes.append(quote)

            return quotes
        else:
            raise Exception('This file can not be read')


if __name__ == '__main__':
    print(TXTIngestor.parse('../_data/DogQuotes/DogQuotesTXT.txt'))
