from ingestorInterface import IngestorInterface
from quotemodel import QuoteModel
import docx


class docxIngestor(IngestorInterface):
    files = ['docx']

    @classmethod
    def parse(cls, path):
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
