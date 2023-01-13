from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file):
        if file.endswith(".csv"):
            with open(file) as csv_file:
                data = csv.DictReader(csv_file)
                return list(data)
        else:
            return "Arquivo no formato incorreto"
