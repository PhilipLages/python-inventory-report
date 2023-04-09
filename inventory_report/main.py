import sys

from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if len(sys.argv) < 3:
        return sys.stderr.write("Verifique os argumentos\n")
    path, report_type = sys.argv[1], sys.argv[2]

    if path.endswith(".csv"):
        importer = CsvImporter
    elif path.endswith(".json"):
        importer = JsonImporter
    elif path.endswith(".xml"):
        importer = XmlImporter

    inventory = InventoryRefactor(importer)
    report = inventory.import_data(path, report_type)

    print(report, end="")
