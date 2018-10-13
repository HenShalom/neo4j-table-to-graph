from propertiesTemplate.property_tester import get_property


class GraphItem:
    def __init__(self, json):
        self.json = json
        self.properties = {}

    def get_columns(self):
        return [prop.key for prop in self.properties]

    def write_csv_row(self, row, writer):
        row_dict = self.generate_row_dict(row)
        writer(row_dict)

    def generate_row_dict(self, row):
        row_dict = dict()
        for prop in self.properties:
            row_dict.update(prop.extract_row(row))
        return row_dict
