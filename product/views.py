
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from logger import log_api

from wb_pars_api_server.settings import LOGS_API, LOGS_PARSER
from product.models import Product

from parsers.wb_parser import get_wb_products
from django.views.decorators.csrf import csrf_exempt

log_api.info('Server is running ')

log_api.info(f"[LOGGER] LOGS_API = {LOGS_API!r}")
log_api.info(f"[LOGGER] LOGS_PARSER = {LOGS_PARSER!r}")

class ParseProduct(APIView):
    def  get(self, request):
        log_api.info(f"GET - products page")
        return render(request, template_name='products_page.html')
    
    @csrf_exempt
    def post(self, request):
        log_api.info(f"GET - products page")
        category = request.data.get('category_name')
        log_api.info(f"POST: products_category: {category}")
        parsed_prods_json = get_wb_products(category)
        prods_json_lst = parsed_prods_json['data']['products']
        print("Len:", len(prods_json_lst))
        
        print(type(prods_json_lst))
        if len(prods_json_lst) > 1:
            print('LEN OK')
            log_api.info('🟢 Products data has been receiver')

        return Response({"products": "parsed_products"}, status=status.HTTP_200_OK)
