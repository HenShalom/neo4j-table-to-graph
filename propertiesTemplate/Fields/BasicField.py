class BasicField:
    def __init__(self, field):
        self.column = field[1:]

    def get_column_value(self, row):
        return row[self.column]
