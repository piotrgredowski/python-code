import pathlib

from divisions import get_divisions_for_country
from divisions import print_divisions
from reader import read_csv
from settings import settings


def main():
    settings.print_app_title()

    path_to_file = str(pathlib.Path(__file__).parent / "00_data.csv")
    data = read_csv(path_to_file)
    for row in data:
        country_code = row.get("CountryCode")
        if (country_code is None) or country_code in settings.skip_country_codes:
            continue
        divisions = get_divisions_for_country(country_code)
        print_divisions(
            country_name=row["Country"],
            capital=row["Capital"],
            divisions=divisions,
        )


if __name__ == "__main__":
    main()
