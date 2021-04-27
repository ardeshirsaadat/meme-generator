from .ingestorInterface import IngestorInterface
from .quotemodel import QuoteModel
import docx


class DOCXIngestor(IngestorInterface):
    """
    This class inherits from
    IngestorInterface class
    and handles 'docx' file types
    """
    files = ['docx']

    @classmethod
    def parse(cls, path):
        """
        Returns a valid QuoteModel
        """
        quotes = []
        if cls.can_ingest(path):
            file_docx = docx.Document(path)
            for paragraph in file_docx.paragraphs:
                parse = paragraph.text.split('-')
                if len(parse) > 1:
                    quote = QuoteModel(parse[0], parse[1])
                    quotes.append(quote)
            return quotes
        else:
            raise Exception('This file can not be read')


if __name__ == '__main__':
    print(docxIngestor.parse('DogQuotesDOCX.docx'))
