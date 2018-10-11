class StringField:
    def __init__(self, key, column):
        self.key = key
        self.column = column

    def extract_row(self, row):
        row_value = row[self.column]
        return {self.key: row_value}

    @staticmethod
    def test(key, value):
        if type(value) == str and value.startswith('@'):
            return StringField(key, value[1:])
        return None
