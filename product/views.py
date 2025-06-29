
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from logger import log_api

from wb_pars_api_server.settings import LOGS_API, LOGS_PARSER
from product.models import Product

from parsers.wb_parser import get_wb_products
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt



log_api.info('🌐 API Server is running ')

log_api.info(f"[LOGGER] LOGS_API = {LOGS_API!r}")
log_api.info(f"[LOGGER] LOGS_PARSER = {LOGS_PARSER!r}")




@method_decorator(csrf_exempt, name='dispatch')
class ParseProduct(APIView):
    def  get(self, request):
        log_api.info(f"GET - products page")
        return render(request, template_name='products_page.html')
    
    def post(self, request):
        log_api.info(f"GET - products page")
        category = request.data.get('category_name')
        log_api.info(f"POST: products_category: {category}")
        parsed_prods_json = get_wb_products(category)
        prods_json_lst = parsed_prods_json['data']['products']
        log_api.info(f"Len: {len(prods_json_lst)}")
        
        response_dict = {"Widlberries parsing products": None}

        ok_data_msg = '🟢 Products data has been received'
        no_data_msg = '🔴 Products data hast not been received'

        if len(prods_json_lst) > 1:
            log_api.info(ok_data_msg)
            response_dict['Widlberries parsing products'] = ok_data_msg
        else:
            log_api.info(no_data_msg)
            response_dict['Widlberries parsing products'] = no_data_msg
            return Response(response_dict, status=status.HTTP_200_OK)
        
        for prod in prods_json_lst:
            product = Product(id=prod['id'],
                              title=prod["name"],
                              price_original=prod["priceU"],
                              price=prod["salePriceU"],
                              rating=prod["rating"],
                              review_amount=prod["feedbacks"],
                              )
            product.save()
        return Response(response_dict, status=status.HTTP_200_OK)
