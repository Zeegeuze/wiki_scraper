import requests
import csv
import json
from bs4 import BeautifulSoup

class Scraping():
    def __init__(self):
        self

    def check_status_valid(self, root):
        '''
        This will check the status code. If the status code is 200, it returns True, otherwise the error will be returned.
        '''
        # query the /status endpoint and get the response
        url = root + "/status"
        response = requests.get(url)

        # check the status_code, return true if valid and the error message if not valid
        if response.status_code == 200:
            return(True)
        else:
            return(response.status_code)


    def set_cookie(self, root):
        '''
        This will set or refresh the cookie every time it is called. It return the session where the cookie is set.
        '''

        cookie_url = "/cookie"
        s = requests.Session()
        s.post(root + cookie_url)
        s.get(root + cookie_url).json()
        return(s)

    def get_wiki_info(self, s, url):
        '''
        Gets the first paragraph of a wikipedia article.
        '''
        response = s.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        paragraphs = soup.find_all('p')
        name = soup.find('h1').text

        for par in  paragraphs:
            bold = par.find_all('b')
            if bold != []:
                first_paragraph_uncleaned = par.text
                first_paragraph = first_paragraph_uncleaned.replace("\xa0", " ")
                break
        return name, first_paragraph

    def get_leaders(self, root):
        '''
        Gives back a list of leaders and their information
        '''

        # 1. Define the urls
        countries_url = "/countries"
        leaders_url = "/leaders"

        # 2. Get the cookies
        s = self.set_cookie(root)

        # 3. Get the countries
        countries = s.get(root + countries_url).json()

        # 4. Get the leaders
        leaders = [s.get(root + leaders_url, params = {"country": country}).json() for country in countries]

        return leaders

    def get_first_paragraph(self, leaders):
        '''
        Give give back a dictionary with all leaders of all the contries of the API.
        '''

        # 1. Create leaders dict
        first_paragraphs = {}

        # 2. get list of urls
        s = requests.Session()

        print_index = 1
        for leaders_country in leaders:
            print(f"Country {print_index} of {len(leaders)} starting")
            print_index += 1

            for leader in leaders_country:
                # get print statements to follow up
                print(f"Starting with: {leader['first_name']} {leader['last_name']}")

                # get first paragraphs
                parag = self.get_wiki_info(s, leader['wikipedia_url'])
                first_paragraphs[parag[0]] = parag[1]
        return first_paragraphs

    def save(self, leaders_per_country):
        # Serializing json
        json_object = json.dumps(leaders_per_country, indent=4)

        # Writing to sample.json
        with open("leaders_data.json", "w") as outfile:
            outfile.write(json_object)
