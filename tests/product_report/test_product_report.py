from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "ChocoBoom",
        "Doces Trint",
        "2023-04-08",
        "2023-12-08",
        "1234567890",
        "Em local refrigerado",
    )

    assert product.id == 1
    assert product.nome_do_produto == "ChocoBoom"
    assert product.nome_da_empresa == "Doces Trint"
    assert product.data_de_fabricacao == "2023-04-08"
    assert product.data_de_validade == "2023-12-08"
    assert product.numero_de_serie == "1234567890"
    assert product.instrucoes_de_armazenamento == "Em local refrigerado"
