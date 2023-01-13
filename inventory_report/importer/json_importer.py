from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file):
        if file.endswith(".json"):
            with open(file) as json_file:
                data = json.DictReader(json_file)
                return list(data)
        else:
            return "Arquivo no formato incorreto"
