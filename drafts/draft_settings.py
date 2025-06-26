import dotenv
import os
from pathlib import Path


dotenv.load_dotenv('.env')


ROOT_DIR = Path(__file__).resolve().parent

DATABASE_DIR = ROOT_DIR / 'data_base'

API_SERVER_DIR = ROOT_DIR / ''

PARSER_DIR = ROOT_DIR / 'parser_wb'

LOGS_DIR = ROOT_DIR / 'logs'

if not os.path.exists(DATABASE_DIR):
    os.makedirs(DATABASE_DIR)

USERAGENT = os.getenv('USERAGENT')
WB_SEARCH_URL = os.getenv('WB_SEARCH_URL')


REQUEST_HEADERS = {
 "User-Agent": USERAGENT,
 "Access-Control-Allow-Credentials": "true",
 "Access-Control-Allow-Headers":"Authorization,Accept,Origin,DNT,User-Agent,Content-Type,Wb-AppType,Wb-AppVersion,Xwbuid,Site-Locale,X-Clientinfo,Storage-Type,Data-Version,Model-Version,__wbl, x-captcha-id",
 "Access-Control-Allow-Methods":"GET,OPTIONS",
 "Access-control-Allow-Origin":"https://www.wildberries.ru",
 "Content-Encoding":"gzip",
 "Content-Type":"application/json charset=utf-8"
 }


REGION_CODE = os.getenv('REGION_CODE')
print(REGION_CODE)