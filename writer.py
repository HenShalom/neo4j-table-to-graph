import csv
import os

from modelLoader.intilizer import data_loader


def get_all_columns(tables, key):
    columns = set()
    print(tables)
    for table in tables:
        items = tables[table][key]
        for item in items:
            columns.update(item.get_columns())
    return list(columns)


def load_tables(models_items, tables_location, output_location):
    tables_file = [pos_json for pos_json in os.listdir(tables_location) if pos_json.endswith('.csv')]
    clear_vertices(output_location)
    clear_edges(output_location)
    columns_v = get_all_columns(models_items, 'vertices')
    columns_e = get_all_columns(models_items, 'edges')
    for table in tables_file:
        if table[:-4] in models_items:
            print(table)
            write_items(models_items[table[:-4]], table[:-4], tables_location, output_location, columns_v, columns_e)


def write_items(items, table, tables_location, output_location, columns_v, columns_e):
    write_vertices_header(columns_v, output_location)
    write_vertices(columns_v, items['vertices'], table, tables_location, output_location)
    write_edges_header(columns_e, output_location)
    write_edges(columns_e, items['edges'], table, tables_location, output_location)


def write_vertices_header(columns, output_location):
    with open('{}/nodes_header.csv'.format(output_location), 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()


def clear_vertices(output_location):
    with open('{}/nodes.csv'.format(output_location), 'w') as csvfile:
        pass


def clear_edges(output_location):
    with open('{}/edges.csv'.format(output_location), 'w') as csvfile:
        pass


def write_vertices(columns, vertices, table, tables_location, output_location):
    with open('{}/nodes.csv'.format(output_location), 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        with open('{}/{}.csv'.format(tables_location, table)) as csvfile_reader:
            reader = csv.DictReader(csvfile_reader)
            for row in reader:
                for vertex in vertices:
                    vertex.write_csv_row(row, writer.writerow)


def write_edges_header(columns, output_location):
    with open('{}/edges_header.csv'.format(output_location), 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()


def write_edges(columns, edges, table, tables_location, output_location):
    with open('{}/edges.csv'.format(output_location), 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        with open('{}/{}.csv'.format(tables_location, table)) as csv_reader:
            reader = csv.DictReader(csv_reader)
            for row in reader:
                for edge in edges:
                    edge.write_csv_row(row, writer.writerow)


def main(model_location, tables_location, output_location):
    models_items = data_loader(model_location)
    load_tables(models_items, tables_location, output_location)
