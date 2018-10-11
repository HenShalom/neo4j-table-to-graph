import BasicField, ConstField


def get_field(value):
    if value.startwith('@'):
        return BasicField(value)
    return ConstField(value)
