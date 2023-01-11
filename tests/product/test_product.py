from inventory_report.inventory.product import Product

test_product = {
    "id": "1",
    "nome_da_empresa": "Empresa Dias",
    "nome_do_produto": "Apple",
    "data_de_fabricacao": "25/12/2022",
    "data_de_validade": "01/01/2023",
    "numero_de_serie": "12345678",
    "instrucoes_de_armazenamento": "deixar na geladeira"
}


def test_cria_produto():
    product = Product(
        test_product["id"],
        test_product["nome_da_empresa"],
        test_product["nome_do_produto"],
        test_product["data_de_fabricacao"],
        test_product["data_de_validade"],
        test_product["numero_de_serie"],
        test_product["instrucoes_de_armazenamento"],
        )

    assert product.id == test_product["id"]
    assert product.nome_do_produto == test_product["nome_da_empresa"]
    assert product.nome_da_empresa == test_product["nome_do_produto"]
    assert product.data_de_fabricacao == test_product["data_de_fabricacao"]
    assert product.data_de_validade == test_product["data_de_validade"]
    assert product.numero_de_serie == test_product["numero_de_serie"]
    assert product.instrucoes_de_armazenamento == "deixar na geladeira"
