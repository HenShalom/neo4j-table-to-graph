from propertiesTemplate.Fields.FieldTester import get_field


class StringProperty:
    def __init__(self, key, field):
        self.key = key
        self.field = field

    def get_value(self, row):
        return self.field.get_column_value(row)

    def extract_row(self, row):
        return {self.key: self.get_value(row)}

    @staticmethod
    def test(key, value):
        if type(value) == str:
            return StringProperty(key, get_field(value))
        return None
