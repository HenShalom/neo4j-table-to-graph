from propertiesTemplate import ObjectProperty, StringProperty, ArrayProperty, EmprtyProperty


def get_property(key, value):
    properties = [StringProperty,
                  ObjectProperty,
                  ArrayProperty,
                  EmprtyProperty]
    
    for prop in properties:
        p = prop.test(key, value)
        if p is not None:
            return p
