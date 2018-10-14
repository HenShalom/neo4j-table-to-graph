import os
from shutil import copyfile


def drop_dup(output_location, output_end_location):
    drop_nodes_dup(output_location, output_end_location)
    drop_edges_dup(output_location, output_end_location)


def drop_nodes_dup(output_location, output_end_location):
    with open(os.path.join(output_end_location, 'nodes_header.csv'), 'r') as f:
        id_index = f.readline()[:-1].split(',').index(':ID')
    with open(os.path.join(output_location, 'nodes.csv'), 'r') as in_file, open(
            os.path.join(output_end_location, 'nodes.csv'), 'w') as out_file:
        node_id = set()
        for line in in_file:
            split_line = line[:-1].split(',')
            if len(split_line) == 1:
                continue
            if split_line[id_index] in node_id:
                continue  # skip duplicate
            node_id.add(split_line[id_index])
            out_file.write(line)


def drop_edges_dup(output_location, output_end_location):
    with open(os.path.join(output_end_location, 'edges_header.csv'), 'r') as f:
        line = f.readline()[:-1].split(',')
        start_index = line.index(':START_ID')
        end_index = line.index(':END_ID')
    with open(os.path.join(output_location, 'edges.csv'), 'r') as in_file, open(
            os.path.join(output_end_location, 'edges.csv'), 'w') as out_file:
        edge_id = set()
        for line in in_file:
            split_line = line[:-1].split(',')
            if len(split_line) == 1:
                continue
            id = split_line[start_index] + split_line[end_index]
            if id in edge_id:
                continue  # skip duplicate
            edge_id.add(id)
            out_file.write(line)


def copy_header_file(output_location, output_end_location):
    copyfile(os.path.join(output_location, 'nodes_header.csv'), os.path.join(output_end_location, 'nodes_header.csv'))
    copyfile(os.path.join(output_location, 'edges_header.csv'), os.path.join(output_end_location, 'edges_header.csv'))
