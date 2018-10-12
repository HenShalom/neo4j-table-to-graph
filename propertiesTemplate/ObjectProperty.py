import constants
from propertiesTemplate.Fields.FieldTester import get_field


class ObjectProperty:
    def __init__(self, key, delimiter, fields):
        self.key = key
        self.delimiter = delimiter
        self.fields = fields

    def get_value(self, row):
        return self.delimiter.join([field.get_value(row) for field in self.fields])

    def extract_row(self, row):
        return {self.key: self.get_value(row)}

    @staticmethod
    def test(key, value):
        if type(value) == dict and 'fields' in value:
            delimiter = value['delimiter'] if 'delimiter' in value else constants.DEFAULT_DELIMITER
            return ObjectProperty(key, delimiter, [get_field(prop) for prop in value['fields']])
        return None
