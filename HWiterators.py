from pprint import pprint
import json


class CountriesIt:

    def __init__(self, path):
        self.path = path

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path) as f:
            json_data = json.load(f)
            i = 0
            countries_dict = {}
            while i < len(json_data):
                country = json_data[i]
                country_name = country['name']['common']
                if ' ' in country_name:
                    country_name = country_name.replace(' ', '_')
                i += 1
                countries_dict[country_name] = f'https://en.wikipedia.org/wiki/{country_name}'
            pprint(countries_dict)
            with open('countries2.json', 'w') as file:
                json.dump(countries_dict, file, ensure_ascii=False, indent=2)


def countries_gen(path):
    with open(path) as f:
        json_data = json.load(f)
    i = 0
    countries_dict = {}
    while i < len(json_data):
        country = json_data[i]
        country_name = country['name']['common']
        if ' ' in country_name:
            country_name = country_name.replace(' ', '_')
        i += 1
        countries_dict[country_name] = f'https://en.wikipedia.org/wiki/{country_name}'
    pprint(countries_dict)
    with open('countries3.json', 'w') as file:
        json.dump(countries_dict, file, ensure_ascii=False, indent=2)


countries_gen('countries.json')
