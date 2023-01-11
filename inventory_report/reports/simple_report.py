from datetime import date as dt
from collections import Counter

#    [
#      {
#        "id": 1,
#        "nome_do_produto": "CADEIRA",
#        "nome_da_empresa": "Forces of Nature",
#        "data_de_fabricacao": "2022-04-04",
#        "data_de_validade": "2023-02-09",
#        "numero_de_serie": "FR48",
#        "instrucoes_de_armazenamento": "Conservar em local fresco"
#      }
#    ]


class SimpleReport:
    @staticmethod
    def generate(file):
        today = dt.today().strftime("%Y-%m-%d")

        manufacturing_dates = [item["data_de_fabricacao"] for item in file]
        oldest_manuf_date = sorted(manufacturing_dates)[0]

        validate_dates = [item["data_de_validade"] for item in file]
        closest_valid_date = [
            sorted(item for item in validate_dates if item > today)[0]
            ]

        companies = [item["nome_da_empresa"] for item in file]
        company_with_most_products = Counter(companies).most_common()
        company, products = company_with_most_products[0]

        return (
            f"Data de fabricação mais antiga: {oldest_manuf_date}\n"
            f"Data de validade mais próxima: {closest_valid_date[0]}\n"
            f"Empresa com mais produtos: {company}"
        )
