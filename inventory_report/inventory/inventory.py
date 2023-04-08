import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path: str, report_type: str) -> str:
        data = []

        if path.endswith(".csv"):
            with open(path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                data = [dict(row) for row in reader]
        elif path.endswith(".json"):
            with open(path) as jsonfile:
                data = json.load(jsonfile)
        elif path.endswith(".xml"):
            with open(path) as xmlfile:
                data = xmltodict.parse(xmlfile.read())["dataset"]["record"]

        if report_type == "simples":
            report = SimpleReport.generate(data)
        else:
            report = CompleteReport.generate(data)

        return report
