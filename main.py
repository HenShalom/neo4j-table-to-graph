from modelLoader.intilizer import data_loader
import csv


def get_all_columns(items):
    columns = set()
    for item in items:
        columns.update(item.get_columns())
    return list(columns)


if __name__ == '__main__':
    edges, vertices = data_loader(r'D:\Wrok\dayJob\tableTransform\data\model')
    fieldnamesV = get_all_columns(vertices)
    print(len(vertices))
    with open('output/nodes_header.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnamesV)
        writer.writeheader()
    with open('output/nodes.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnamesV)
        with open('data/csv/people.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                for vertex in vertices:
                    vertex.write_csv_row(row, writer.writerow)
    fieldnamesE = get_all_columns(edges)
    with open('output/edges_header.csv', 'w') as csvfile2:
        writer = csv.DictWriter(csvfile2, fieldnames=fieldnamesE)
        writer.writeheader()
    with open('output/edges.csv', 'w') as csvfile2:
        writer = csv.DictWriter(csvfile2, fieldnames=fieldnamesE)
        with open('data/csv/people.csv') as csvfile2:
            reader = csv.DictReader(csvfile2)
            for row in reader:
                for edge in edges:
                    edge.write_csv_row(row, writer.writerow)
