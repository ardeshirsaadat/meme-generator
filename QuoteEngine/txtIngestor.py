from .ingestorInterface import IngestorInterface
from .quotemodel import QuoteModel


class TXTIngestor(IngestorInterface):
    """
    This class inherits from
    IngestorInterface class,
    and handles 'txt' file types
    """
    files = ['txt']

    @classmethod
    def parse(cls, path):
        """
        Returns a valid QuoteModel
        """
        quotes = []
        if cls.can_ingest(path):
            r = open(path, 'r')
            for line in r.readlines():
                line = line.strip('\n\r').strip()
                line = line.split('-')
                if len(line) > 1:
                    quote = QuoteModel(line[0], line[1])
                    quotes.append(quote)
            r.close()
            return quotes
        else:
            raise Exception('This file can not be read')


if __name__ == '__main__':
    print(TXTIngestor.parse('../_data/DogQuotes/DogQuotesTXT.txt'))
