from propertiesTemplate.property_tester import get_property


class Vertex:
    def __init__(self, vertexJSON):
        self.properties = generate_vertex_properties(vertexJSON)

    def get_columns(self):
        return [prop['key'] for prop in self.properties]

    def write_csv_row(self, row, writer):
        row_dict = self.generate_row_dict(row)
        writer(row_dict)

    def generate_row_dict(self, row):
        row_dict = dict()
        for prop in self.properties:
            row_dict.update(prop.extract_row(row))
        return row_dict


def generate_vertex_properties(vertexJSON):
    properties = [get_property(':ID', vertexJSON['id']),
                  get_property(':Label', vertexJSON['label'])]
    if 'properties' not in vertexJSON: return properties
    for prop in vertexJSON["properties"]:
        properties.append(get_property(prop, vertexJSON["properties"][prop]))
    return properties
