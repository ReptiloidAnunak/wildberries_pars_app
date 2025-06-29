import dotenv
import os
from pathlib import Path


dotenv.load_dotenv('.env')


ROOT_DIR = Path(__file__).resolve().parent

PARSER_DIR = ROOT_DIR / 'parser_wb'

LOGS_DIR = ROOT_DIR / 'logs'

WB_SEARCH_URL = os.getenv('WB_SEARCH_URL')

REGION_CODE = os.getenv('REGION_CODE')

PROXY_ST_1 = os.getenv('PROXY_ST_1')
PROXY_ST_2 = os.getenv('PROXY_ST_2')


PROXY_LIST = [
    {
        "http": f"http://{PROXY_ST_1}",
        "https": f"http://{PROXY_ST_1}"
    },
    {
        "http": f"http://{PROXY_ST_2}",
        "https": f"http://{PROXY_ST_2}"
    }
]


USER_AGENTS = [
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:139.0) Gecko/20100101 Firefox/139.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; Pixel 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.133 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13.4; rv:115.0) Gecko/20100101 Firefox/115.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/99.0.4844.51"
]
