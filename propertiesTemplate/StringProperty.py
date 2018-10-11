from propertiesTemplate.Fields.FieldTester import get_field


class StringProperty:
    def __init__(self, key, field):
        self.key = key
        self.field = field

    def extract_row(self, row):
        row_value = self.field.get_column_value(row)
        return {self.key: row_value}

    @staticmethod
    def test(key, value):
        if type(value) == str:
            return StringProperty(key, get_field(value))
        return None
