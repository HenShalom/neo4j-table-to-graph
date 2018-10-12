from propertiesTemplate.Fields.FieldTester import get_field


class ArrayProperty:
    def __init__(self, key, fields):
        self.key = key
        self.fields = fields

    def get_value(self, row):
        return [field.get_value(row) for field in self.fields]

    def extract_row(self, row):
        return {self.key: self.get_value(row)}

    @staticmethod
    def test(key, value):
        if type(value) == list:
            return ArrayProperty(key, [get_field(prop) for prop in value])
        return None
