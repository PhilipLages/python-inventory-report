from pytest import fixture
from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


@fixture
def products():
    return [
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


def test_decorar_relatorio(products):

    colored_report = ColoredReport(SimpleReport).generate(products)

    expected_report = (
        "\033[32mData de fabricação mais antiga:\033[0m "
        "\033[36m2023-04-08\033[0m\n"
        "\033[32mData de validade mais próxima:\033[0m "
        "\033[36m2023-12-08\033[0m\n"
        "\033[32mEmpresa com mais produtos:\033[0m "
        "\033[31mChocoBoom\033[0m"
    )

    assert colored_report == expected_report
