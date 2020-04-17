import requests
import json
from bs4 import BeautifulSoup

page_content = requests.get('https://www.mohfw.gov.in/').content


class IndiaData:

    def __init__(self, page):
        self.page = page
        self.soup = BeautifulSoup(self.page, 'html.parser')
        self.all_state_data = []

    @property
    def state_data(self):
        locator = 'tbody tr td'
        for state in self.soup.select(locator):
            self.all_state_data.append(state.string)
        column_number = 5
        subList = [self.all_state_data[n: n + column_number] for n in range(0, len(self.all_state_data), column_number)]
        return subList

    def state_wise_date(self):
        all_data = self.state_data
        total_data = all_data.pop()
        my_dict = {}
        for state in all_data:
            no, state_name, total, cured, death = state
            my_dict[state_name] = {
                'state':  state_name,
                'Total Confirmed cases': total,
                'Cured/Discharged': cured,
                'Death': death
            }
        with open('covid.json', 'r+') as file:
            json.dump(my_dict, file)


data = IndiaData(page_content)
data.state_wise_date()

