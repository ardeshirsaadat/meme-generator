from .ingestorInterface import IngestorInterface
from .quotemodel import QuoteModel
import subprocess
import random


class PDFIngestor(IngestorInterface):
    """
    This class inherits from
    IngestorInterface class
    and handles 'pdf' file types
    """
    files = ['pdf']

    @classmethod
    def parse(cls, path):
        """
        Returns a valid QuoteModel
        """
        quotes = []
        if cls.can_ingest(path):
            tmp = f'../tmp/{random.randint(1,100)}.txt'
            subprocess.run(['pdftotext', '-simple', path, tmp])
            r = open(tmp, 'r')
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
    print(PDFIngestor.parse('DogQuotesPDF.pdf'))
