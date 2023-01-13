from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.csv_importer import JsonImporter


class Inventory:
    @classmethod
    def get_path_report(cls, path):
        report = []

        if path.endswith(".csv"):
            report = CsvImporter.import_data(path)
        elif path.endswith(".json"):
            report = JsonImporter.import_data(path)
        return report

    @classmethod
    def import_data(cls, path, type):
        report = Inventory.get_path_report(path)

        if type == "simples":
            return SimpleReport.generate(report)
        elif type == "completo":
            return CompleteReport.generate(report)
        else:
            return "Arquivo no formato incorreto"
