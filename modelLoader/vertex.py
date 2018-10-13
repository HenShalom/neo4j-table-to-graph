from propertiesTemplate.property_tester import get_property
from modelLoader.graphItem import GraphItem


class Vertex(GraphItem):
    def __init__(self, vertexJSON):
        super().__init__(vertexJSON)
        self.properties = generate_vertex_properties(vertexJSON)


def generate_vertex_properties(vertexJSON):
    properties = [get_property(':ID', vertexJSON['id']),
                  get_property(':LABEL', vertexJSON['label'])]
    if 'properties' not in vertexJSON: return properties
    for prop in vertexJSON["properties"]:
        properties.append(get_property(prop, vertexJSON["properties"][prop]))
    return properties
