class ConstField:
    def __init__(self, field):
        self.column = field

    def get_column_value(self, row):
        return self.column
