from propertiesTemplate.EmptyProperty import EmptyProperty
from propertiesTemplate.ObjectProperty import ObjectProperty
from propertiesTemplate.StringProperty import StringProperty
from propertiesTemplate.ArrayProperty import ArrayProperty


def get_property(key, value):
    properties = [StringProperty,
                  ObjectProperty,
                  ArrayProperty,
                  EmptyProperty]

    for prop in properties:
        p = prop.test(key, value)
        if p is not None:
            return p
