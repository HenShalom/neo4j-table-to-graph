class ConstField:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def extract_row(self, row):
        return {self.key: self.value}

    @staticmethod
    def test(key, value):
        if type(value) == str and not value.startswith('@'):
            return ConstField(key, value)
        return None
