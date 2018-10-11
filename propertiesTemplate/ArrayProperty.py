from property_tester import get_property


class ObjectProperty:
    def __init__(self, key, fields):
        self.key = key
        self.fields = fields

    def get_value(self, row):
        return [field.get_column_value(row) for field in self.fields]

    def extract_row(self, row):
        return {self.key: self.get_value(row)}

    @staticmethod
    def test(key, value):
        if type(value) == list:
            return ObjectProperty(key, [get_property('', prop) for prop in value])
        return None
