from .importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(self, file: str):
        if file.endswith(".xml"):
            with open(file) as xmlfile:
                data = xmltodict.parse(xmlfile.read())["dataset"]["record"]
                return data
        else:
            raise ValueError("Arquivo inválido")
