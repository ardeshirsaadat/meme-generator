from .ingestorInterface import IngestorInterface
from .quotemodel import QuoteModel
import subprocess
import random
import os


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
            tmp = f'./{random.randint(1,100)}.txt'
            subprocess.call(['pdftotext', path, tmp])
            # cmd = r"""{} "{}" "{}" -enc UTF-8""".format('pdftotext', path, tmp)
            # subprocess.run(cmd, shell=True, stderr=subprocess.STDOUT)
            r = open(tmp, 'r')
            for line in r.readlines():
                line = line.strip('\n\r').strip()
                line = line.split('-')
                if len(line) > 1:
                    quote = QuoteModel(line[0], line[1])
                    quotes.append(quote)
            r.close()
            # os.remove(tmp)
            return quotes
        else:
            raise Exception('This file can not be read')


if __name__ == '__main__':
    print(PDFIngestor.parse('DogQuotesPDF.pdf'))
