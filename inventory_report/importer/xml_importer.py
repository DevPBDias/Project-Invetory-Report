from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


# https://www.guru99.com/manipulating-xml-with-python.html
# https://www.geeksforgeeks.org/reading-and-writing-xml-files-in-python/
class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file):
        if file.endswith(".xml"):
            tree = ET.parse(file)
            root = tree.getroot()
            data = []
            for elem in root:
                data.append({response.tag: response.text for response in elem})
            return data
        raise ValueError("Arquivo inválido")
