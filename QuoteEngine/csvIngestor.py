from .ingestorInterface import IngestorInterface
from .quotemodel import QuoteModel
import csv


class CSVIngestor(IngestorInterface):
    """
    This class inherits from
    IngestorInterface class
    and handles 'csv' file types
    """
    files = ['csv']

    @classmethod
    def parse(cls, path):
        """
        Returns a valid QuoteModel
        """
        quotes = []
        if cls.can_ingest(path):
            with open(path, 'r') as file:
                csvFile = csv.DictReader(file)
                for line in csvFile:
                    quote = QuoteModel(line['body'], line['author'])
                    quotes.append(quote)
            return quotes
        else:
            raise Exception('This file can not be read')


if __name__ == '__main__':
    print(CSVIngestor.parse('../_data/DogQuotes/DogQuotesCSV.csv'))
