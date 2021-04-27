
from .ingestorInterface import IngestorInterface
from .csvIngestor import CSVIngestor
from .docxIngestor import DOCXIngestor
from .pdfIngestor import PDFIngestor
from .txtIngestor import TXTIngestor


class Ingestor(IngestorInterface):
    files = ['pdf', 'txt', 'docx', 'csv']

    @classmethod
    def parse(cls, path):

        extenstion = path.split('.')[-1]
        try:
            if extenstion == 'pdf':
                return PDFIngestor.parse(path)
            elif extenstion == 'txt':
                return TXTIngestor.parse(path)
            elif extenstion == 'docx':
                return DOCXIngestor.parse(path)
            elif extenstion == 'csv':
                return CSVIngestor.parse(path)
            else:
                raise Exception('File not supported')
        except Exception as e:
            print(e)
