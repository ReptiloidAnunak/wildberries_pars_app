from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from logger import log_api
import math
from collections import Counter

from wb_pars_api_server.settings import LOGS_API, LOGS_PARSER
from product.models import Product

from parsers.wb_parser import get_wb_products
from product.filter import filter_products
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

log_api.info('🌐 API Server is running ')
log_api.info(f"[LOGGER] LOGS_API = {LOGS_API!r}")
log_api.info(f"[LOGGER] LOGS_PARSER = {LOGS_PARSER!r}")


@method_decorator(csrf_exempt, name='dispatch')
class ParseProduct(APIView):
    def get(self, request):
        log_api.info(f"GET - products page")
        log_api.info(f"GET QUERY PARAMS: {request.GET.dict()}")

        category = request.GET.get('category', '')
        price_min = request.GET.get('price_min', '')
        price_max = request.GET.get('price_max', '')
        rating = request.GET.get('rating', '')
        review = request.GET.get('review', '')
        sort = request.GET.get('sort', '')

        log_api.info(f"GET - {category} {price_min} {price_max} {rating} {review} {sort}")


        products_all = Product.objects.all()
        prices_all = [p.price for p in products_all if p.price is not None]
        
        bin_size = 500
        bins = [bin_size * math.floor(p / bin_size) for p in prices_all]
        hist = Counter(bins)
        labels = [f"{b}-{b + bin_size - 1}" for b in sorted(hist)]

        prices_labels = [f"{b}-{b + bin_size - 1}" for b in sorted(hist)]
        prices_values = [hist[b] for b in sorted(hist)]


        products = filter_products(
            category=category,
            price_min=price_min,
            price_max=price_max,
            rating=rating,
            review=review,
            sort=sort
        )

        page = request.GET.get('page', 1)
        paginator = Paginator(products, 20)

        try:
            products_page = paginator.page(page)
        except PageNotAnInteger:
            products_page = paginator.page(1)
        except EmptyPage:
            products_page = paginator.page(paginator.num_pages)


        labels = [f"rating: {p.rating}\nid: {p.id}" for p in products if p.rating is not None]
        discounts = [(p.price_original - p.price) for p in products if p.price_original and p.price]

        return render(request, 'products_page.html', {
            'products': products_page,
            'category': category,
            'price_min': price_min,
            'price_max': price_max,
            'rating': rating,
            'review': review,
            'sort': sort,
            'request': request,
            'labels': labels,
            'discounts': discounts,
            'prices_labels': prices_labels,
            'prices_values': prices_values,
        })

    def post(self, request):
        Product.objects.all().delete()

        category = request.data.get('category_name', '')
        price_min = request.data.get('price_min', '')
        price_max = request.data.get('price_max', '')
        rating = request.data.get('rating', '')
        review = request.data.get('review', '')
        sort = request.data.get('sort', '')

        log_api.info(f"POST:\n\nproducts_category: {category}, price_min: {price_min}, price_max: {price_max} rating: {rating} review: {review} sort: {sort}\n\n")

        parsed_prods_json = get_wb_products(category)
        try:
            prods_json_lst = parsed_prods_json['data']['products']
        except KeyError:
            prods_json_lst = []
            log_api.error('Restrictions from Wildberries server. Try again')

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
            product = Product(
                id=prod['id'],
                title=prod["name"],
                price_original=prod["priceU"] / 100,
                price=prod["salePriceU"] / 100,
                rating=prod["rating"],
                review_amount=prod["feedbacks"],
            )
            product.save()

        valid_sort_fields = {'price_original', 'price', 'rating', 'review'}

        if sort:
            sort_field = sort.lstrip('-')
            if sort_field in valid_sort_fields:
                products = products.order_by(sort)

        params = {
            'category': category,
            'price_min': price_min,
            'price_max': price_max,
            'rating': rating,
            'review': review,
            'sort': sort
        }
        
        query_string = '&'.join([f'{k}={v}' for k, v in params.items()])

        url = reverse('products-list')
        if query_string:
            url += '?' + query_string
        return redirect(url)
