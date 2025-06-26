import requests
from fake_useragent import UserAgent
from settings import REQUEST_HEADERS, WB_SEARCH_URL, REGION_CODE
import json

user_agent = UserAgent()


import requests


def run_wb_parsing(query: str):
    url = WB_SEARCH_URL
    print(WB_SEARCH_URL)
    
    params = {
    "ab_testing": False,
    "appType": 1,
    "curr": "rub",
    "dest": REGION_CODE,
    "query": query,
    "resultset": "catalog",
    "sort": "popular",
    "spp": 30,
    "page": 1
    }

    headers = REQUEST_HEADERS
    response = requests.get(url, 
                            params=params, 
                            headers=headers)
    
    data = response.json()
    print(data)

    with open("result.json", "w") as file:
        file.write(json.dumps(data))


def run_parser_mod():
    run_wb_parsing("кастрюля")



if __name__ == '__main__':
    run_parser_mod()