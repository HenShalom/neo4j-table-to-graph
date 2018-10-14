from MainLogic.writer import main
from MainLogic.postProcessing import drop_dup, copy_header_file

if __name__ == '__main__':
    model_location = r'.\data\model'
    tables_location = r'.\data\csv'
    output_location = r'.\outputTemp'
    output_end_location = r'.\output'
    main(model_location, tables_location, output_location)
    copy_header_file(output_location, output_end_location)
    drop_dup(output_location, output_end_location)
