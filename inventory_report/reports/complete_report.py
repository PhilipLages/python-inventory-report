from typing import List
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, companies_data: List[dict]) -> str:
        simple_report = SimpleReport.generate(companies_data)

        complete_report = (
            f"{simple_report}\n" "Produtos estocados por empresa:\n"
        )

        for company, count in cls.get_products_by_company(
            companies_data
        ).items():
            complete_report += f"- {company}: {count}\n"

        return complete_report
