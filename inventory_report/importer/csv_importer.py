from .importer import Importer
from csv import DictReader


class CsvImporter(Importer):
    @classmethod
    def import_data(self, file: str):
        if file.endswith(".csv"):
            with open(file, newline='') as csvfile:
                reader = DictReader(csvfile)
                data = [dict(row) for row in reader]
                return data
        else:
            raise ValueError("Arquivo inválido")
