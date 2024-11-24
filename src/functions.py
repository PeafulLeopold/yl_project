import csv


def to_list(path_to_file):
    with open(path_to_file, encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')
        result = [row for row in reader]
    return result
