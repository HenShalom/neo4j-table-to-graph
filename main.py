from writer import main
from more_itertools import unique_everseen

if __name__ == '__main__':
    model_location = r'.\data\model'
    tables_location = r'.\data\csv'
    output_location = r'.\outputTemp'
    output_end_location = r'.\output'
    main(model_location, tables_location, output_location)
    for item in ['edges', 'nodes', 'nodes_header', 'edges_header']:
        with open(output_location + '\\' + item + '.csv', 'r') as r, open(output_end_location + '\\' + item + '.csv',
                                                                          'w') as w:
            w.writelines(unique_everseen(r))
