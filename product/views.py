
from django.shortcuts import render
from product.models import Product
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from logger import log_api
from wb_pars_api_server.settings import LOGS_API, LOGS_PARSER
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
        parsed_products = get_wb_products(category)
        print(parsed_products)
        log_api.info(f"POST: products_category: {category}")
        return Response({"products": "parsed_products"}, status=status.HTTP_200_OK)
