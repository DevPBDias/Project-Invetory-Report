from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, file):
        first_report = super().generate(file)
        second_report = ""
        for company, qty_products in cls.company_with_products(file).items():
            second_report += f"- {company}: {qty_products}\n"

        return (
            f"{first_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{second_report}"
            )
