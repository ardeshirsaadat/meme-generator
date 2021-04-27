from abc import ABC, abstractmethod


class IngestorInterface(ABC):
    """
    Abstract interface to be inherited
    to absorb different file types
    """
    files = []

    @classmethod
    def can_ingest(cls, path):
        """
        Returns a boolean whether
        a file type can be ingested
        by this class
            Parameters:
                    path (str): A path file

            Returns:
                    Boolean
        """
        file_format = path.split('.')[-1]
        return file_format in cls.files

    @classmethod
    @abstractmethod
    def parse(cls, path):
        """
        Returns a parsed version of
        a file type
        """
    pass
