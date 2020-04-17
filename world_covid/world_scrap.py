import requests
from bs4 import BeautifulSoup
import json

content = requests.get('https://www.worldometers.info/coronavirus/').content
continents = ['North America', 'Europe', 'Asia', 'South America', 'Australia/Oceania', 'Africa']


class WorldData:

    def __init__(self, page):
        self.page = page
        self.soup = BeautifulSoup(self.page, 'html.parser')

    @property
    def world_data(self):
        raw_data = self.soup.select('tbody tr td')
        hey = [data.string for data in raw_data]
        fields = 13
        new_list = [hey[n:n + fields] for n in range(0, len(hey), fields)]
        return new_list

    def country_data(self):
        all_data = self.world_data
        my_dict = {}
        for country_name, total, newcases, totaldeaths, nd, recovered, ac, sc, tc, deaths, tests, tt, continent in all_data:
            if country_name != 'Total:' and country_name is not None:
                if recovered is None:
                    recovered = 'Zero'
                if totaldeaths is None:
                    totaldeaths = 'Zero'
                if country_name not in my_dict.keys():
                    my_dict[country_name] = {
                        'Country_name': country_name,
                        'Total cases': total,
                        'Deaths': totaldeaths,
                        'Recovered': recovered
                    }
        with open('world.json', 'r+') as file:
            json.dump(my_dict, file)


data = WorldData(content)
data.country_data()

