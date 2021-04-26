
from ingestorInterface import ingestorInterface


def pick_strategy(unit):
    if unit == 'fahrenheit':
        return FahrenheitToCelsiusConverter
    else:
        return CelsiusToFahrenheitConverter


def smart_convert(temp, unit):
    strategy = pick_strategy(unit)
    result = strategy.convert(32)
    print(result)


class Ingestor(ingestorInterface):
    files = ['pdf', 'txt', 'docx', 'csv']

    @classmethod
    def parse(cls, path):
        if cls.can_ingest(path):
            extenstion = path.split('.')[-1]
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
