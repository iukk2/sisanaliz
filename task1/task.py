import pandas

def main(path, row_number, column_number):
    csv_file = pandas.read_csv(path, header = None)
    return csv_file[column_number - 1][row_number - 1]
