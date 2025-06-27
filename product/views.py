
from django.shortcuts import render
from product.models import Product
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from logger import log_api
from wb_pars_api_server.settings import LOGS_API, LOGS_PARSER

log_api.info('Server is running ')

log_api.info(f"[LOGGER] LOGS_API = {LOGS_API!r}")
log_api.info(f"[LOGGER] LOGS_PARSER = {LOGS_PARSER!r}")

class ParseProduct(APIView):
    def  get(self, request):
        return render(request, template_name='products_page.html')

    def post(self, request):
        category = request.data.get('category_name')
        log_api.info(f"POST: products category {category}")
        return Response({"message": "Data received"}, status=status.HTTP_200_OK)
