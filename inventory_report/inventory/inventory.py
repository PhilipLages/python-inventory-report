import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path: str, report_type: str) -> str:
        data = []
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [dict(row) for row in reader]

        if report_type == "simples":
            report = SimpleReport.generate(data)
        else:
            report = CompleteReport.generate(data)

        return report
