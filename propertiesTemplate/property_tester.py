from propertiesTemplate import ObjectProperty, StringProperty


def get_property(key, value):
    properties = [ObjectProperty, StringProperty]
    for prop in properties:
        p = prop.test(key, value)
        if p is not None:
            return p
