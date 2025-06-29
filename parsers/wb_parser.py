import random
import requests
from .config import PROXY_LIST, USER_AGENTS
import json
import random


def get_wb_products(query: str, page=1):
    url = "https://search.wb.ru/exactmatch/ru/common/v4/search"
    user_agent = random.choice(USER_AGENTS)
    params = {
        "query": query,
        "resultset": "catalog",
        "sort": "popular",
        "page": page,
        "spp": 30,
        "appType": 1,
        "curr": "rub",
        "dest": 1234567
    }

    headers = {
        "User-Agent": user_agent,
        "Accept": "*/*",
        "Origin": "https://www.wildberries.ru",
        "Referer": "https://www.wildberries.ru/",
    }
    

    proxy = random.choice(PROXY_LIST)

    response = requests.get(url, headers=headers, params=params, proxies=proxy, timeout=10)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    data = get_wb_products("смартфон", page=1)
    result_json = json.dumps(data, indent=2, ensure_ascii=False)

    # print(result_json)

    # with open('result.json', 'w') as file:
    #     file.write(result_json)