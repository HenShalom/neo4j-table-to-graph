from propertiesTemplate import ObjectProperty, StringProperty, ArrayProperty


def get_property(key, value):
    properties = [ObjectProperty, StringProperty, ArrayProperty]
    for prop in properties:
        p = prop.test(key, value)
        if p is not None:
            return p
