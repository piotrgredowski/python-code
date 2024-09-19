import csv
import pathlib


def read_csv(path_to_file: str):
    with open(path_to_file) as file:
        reader = csv.DictReader(file)
        data = list(reader)

    return data  # noqa: RET504


path_to_file = str(pathlib.Path(__file__).parent / "00_data.csv")
print("====================================")
print(read_csv(path_to_file))
print("====================================")
