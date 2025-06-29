import requests
from fake_useragent import UserAgent

from wb_pars_api_server.settings import REQUEST_HEADERS, WB_SEARCH_URL, REGION_CODE
from logger import log_parser
import json


user_agent = UserAgent()


import requests


def run_wb_parsing(query: str):
    log_parser.info("Run Wieldbrerries parser")
    log_parser.info(f'Category recieved: {query}')
    
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
    data_json = response.json()
    
    log_parser.info(str(data_json))
    return data_json

    # with open("result.json", "w") as file:
    #     file.write(json.dumps(response.json()))

