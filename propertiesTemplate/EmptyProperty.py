class EmptyProperty:
    def __init__(self, key):
        self.key = key

    def get_value(self, row):
        return ''

    def extract_row(self, row):
        return {}

    @staticmethod
    def test(key, value):
        return EmptyProperty(key)
