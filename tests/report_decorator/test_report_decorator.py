from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():
    products = [
        {
            "id": 1,
            "nome_da_empresa": "ChocoBoom",
            "nome_do_produto": "Chocolate",
            "data_de_fabricacao": "2023-04-08",
            "data_de_validade": "2023-12-08",
            "numero_de_serie": "1234567890",
            "instrucoes_de_armazenamento": "Em local refrigerado",
        },
    ]

    colored_report = ColoredReport(SimpleReport).generate(products)

    green = "\033[32m"
    red = "\033[31m"
    blue = "\033[36m"
    reset = "\033[0m"

    fabrication_text = "Data de fabricação mais antiga: "
    expiration_text = "Data de validade mais próxima: "
    company_text = "Empresa com mais produtos: "
    fabrication_date = "2023-04-08"
    expiration_date = "2023-12-08"
    company_name = "ChocoBoom"

    assert colored_report == (
        f"{green}{fabrication_text}{reset}{blue}{fabrication_date}{reset}\n"
        f"{green}{expiration_text}{reset}{blue}{expiration_date}{reset}\n"
        f"{green}{company_text}{reset}{red}{company_name}{reset}"
    )
