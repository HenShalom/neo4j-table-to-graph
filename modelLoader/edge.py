from propertiesTemplate.property_tester import get_property
from modelLoader.graphItem import GraphItem


class EDGE(GraphItem):
    def __init__(self, edgeJSON):
        super().__init__(edgeJSON)
        self.properties = generate_edge_properties(edgeJSON)


def generate_edge_properties(edgeJSON):
    start_id, end_id = get_edge_ids(edgeJSON)
    properties = [get_property(':START_ID', start_id),
                  get_property(':END_ID', end_id),
                  get_property(':TYPE', edgeJSON['label'])]
    if 'properties' not in edgeJSON: return properties
    for prop in edgeJSON["properties"]:
        properties.append(get_property(prop, edgeJSON["properties"][prop]))
    return properties


def get_edge_ids(edgeJSON):  # TODO:fix the direction alg
    start_id = edgeJSON['id'][0]
    end_id = edgeJSON['id'][1]
    return start_id, end_id
