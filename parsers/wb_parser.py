import random
import requests
from .config import PROXY_LIST, USER_AGENTS
from logger import log_parser
import json
import random

# Wildberries parser to fetch product data based on a search query.
def get_wb_products(query: str, page=1):
    log_parser.info('▶️ Running Wildberries parser ...')

    url = "https://search.wb.ru/exactmatch/ru/common/v4/search"
    user_agent = random.choice(USER_AGENTS)
    log_parser.info(f"User-Agent:\n\n{user_agent}\n\n")

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

    log_parser.info(f"Request params:\n\n{params}\n\n")

    headers = {
        "User-Agent": user_agent,
        "Accept": "*/*",
        "Origin": "https://www.wildberries.ru",
        "Referer": "https://www.wildberries.ru/",
    }

    log_parser.info(f"Reques url: {url}")

    proxy = random.choice(PROXY_LIST)
    response = requests.get(url, headers=headers, params=params, proxies=proxy, timeout=10)
    log_parser.info(f"Wildberries Response Status: {response.status_code}")
    response.raise_for_status()
    return response.json()


# if __name__ == "__main__":
#     data = get_wb_products("смартфон", page=1)
#     result_json = json.dumps(data, indent=2, ensure_ascii=False)

#     print(result_json)

