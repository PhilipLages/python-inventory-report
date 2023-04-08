from .importer import Importer
from json import loads


class JsonImporter(Importer):
    @classmethod
    def import_data(self, file: str):
        if file.endswith(".json"):
            with open(file) as jsonfile:
                data = loads(jsonfile.read())
                return data
        else:
            raise ValueError("Arquivo inválido")
