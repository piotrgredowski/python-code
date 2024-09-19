import argparse

import httpx


def _get_url_for_country(country_code: str):
    return f"https://rawcdn.githack.com/kamikazechaser/administrative-divisions-db/master/api/{country_code}.json"


def get_divisions_for_country(country_code: str):
    return httpx.get(_get_url_for_country(country_code)).json()


def print_divisions(*, country_name: str, divisions: list[str], capital: str | None = None):
    print("====================================")
    capital_part = f" ({capital})" if capital else ""
    print(f"Divisions for {country_name}{capital_part}:")
    for division in divisions:
        print(f"- {division}")
    print("====================================")


argparser = argparse.ArgumentParser()

argparser.add_argument("--country", help="Country code to get divisions for", default="PL")
argparser.add_argument("--pretty", help="Pretty print the output", action="store_true")
args = argparser.parse_args()

divisions = get_divisions_for_country(args.country)

if args.pretty:
    print_divisions(country_name=args.country, divisions=divisions)
else:
    print(divisions)
