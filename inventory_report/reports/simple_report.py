import datetime
from typing import List


class SimpleReport:
    @classmethod
    def get_company_with_most_products(cls, reports: List[dict]) -> str:
        company_counts = {}

        for report in reports:
            company_name = report["nome_da_empresa"]
            if company_name in company_counts:
                company_counts[company_name] += 1
            else:
                company_counts[company_name] = 1

        company_with_most_products = max(
            company_counts, key=company_counts.get
        )
        return company_with_most_products

    @classmethod
    def get_oldest_manufacturing_date(cls, reports: List[dict]) -> str:
        oldest_date = datetime.datetime.now()

        for report in reports:
            manufacturing_date_str = report["data_de_fabricacao"]
            manufacturing_date = datetime.datetime.strptime(
                manufacturing_date_str, "%Y-%m-%d"
            )
            if manufacturing_date < oldest_date:
                oldest_date = manufacturing_date

        oldest_date_str = oldest_date.strftime("%Y-%m-%d")
        return oldest_date_str

    @classmethod
    def get_closest_expiration_date(cls, reports: List[dict]) -> str:
        now = datetime.datetime.now()
        closest_date = datetime.datetime.max

        for report in reports:
            expiration_date_str = report["data_de_validade"]
            expiration_date = datetime.datetime.strptime(
                expiration_date_str, "%Y-%m-%d"
            )
            if expiration_date > now and expiration_date < closest_date:
                closest_date = expiration_date

        closest_date_str = closest_date.strftime("%Y-%m-%d")
        return closest_date_str

    @classmethod
    def generate(cls, reports: List[dict]) -> str:
        company_with_most_products = cls.get_company_with_most_products(
            reports
        )

        oldest_manufacturing_date = cls.get_oldest_manufacturing_date(reports)
        closest_expiration_date = cls.get_closest_expiration_date(reports)

        report = (
            f"Data de fabricação mais antiga: {oldest_manufacturing_date}\n"
        )
        report += f"Data de validade mais próxima: {closest_expiration_date}\n"
        report += f"Empresa com mais produtos: {company_with_most_products}"

        return report
