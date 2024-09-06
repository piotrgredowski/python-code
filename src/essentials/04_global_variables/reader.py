import pathlib
import csv

def read_csv(path_to_file: str):
    with open(path_to_file, mode='r') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    return data


path_to_file = str(pathlib.Path(__file__).parent / "00_data.csv")
print("====================================")
print(read_csv(path_to_file))
print("====================================")

