from propertiesTemplate.Fields.BasicField import BasicField
from propertiesTemplate.Fields.ConstField import ConstField


def get_field(value):
    if value[0] == '@':
        return BasicField(value)
    return ConstField(value)
