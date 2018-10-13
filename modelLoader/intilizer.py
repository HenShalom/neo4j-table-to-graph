import os, json
from modelLoader.vertex import Vertex


def data_loader(models_path):
    json_files = [pos_json for pos_json in os.listdir(models_path) if pos_json.endswith('.json')]
    edges, vertices = [], []
    for file in json_files:
        with open(os.path.join(models_path, file)) as json_file:
            model = json.load(json_file)
            new_edges, new_vertices = extract_data(model)
            edges += new_edges
            vertices += new_vertices
    return edges, vertices


def extract_data(model):
    vertices = []
    edges = []
    for vertex in model['vertices']:
        vertices.append(Vertex(vertex))
        for edge in vertex['edges']:
            # append edge when
            vertices.append(Vertex(edge['vertex']))
    return edges, vertices
