

from logger import log_api
from product.models import Product


def filter_products(request) -> dict:

    category = request.GET.get('category')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    rating = request.GET.get('rating')
    review = request.GET.get('review')
    

    log_api.info(f"GET - {category} {price_min} {price_max} {rating} {review}")

    products = Product.objects.all()
    if price_min:
        try:
            products = products.filter(price__gte=float(price_min))
        except ValueError:
            pass

    if price_max:
        try:
            products = products.filter(price__lte=float(price_max))
        except ValueError:
            pass

    if rating:
        try:
            products = products.filter(rating__gte=float(rating))
        except ValueError:
            pass

    if review:
        try:
            products = products.filter(review_amount__gte=int(review))
        except ValueError:
            pass
    
    sort_mapping = {
        'review': 'review_amount',
        'rating': 'rating',
        'price': 'price',
        'price_original': 'price_original'
    }

    sort = request.GET.get('sort')
    actual_sort_field = None

    if sort:
        reverse = sort.startswith('-')
        clean_sort = sort.lstrip('-')

        if clean_sort in sort_mapping:
            actual_sort_field = sort_mapping[clean_sort]
            if reverse:
                actual_sort_field = '-' + actual_sort_field


    if actual_sort_field:
        products = products.order_by(actual_sort_field)

    return {
            'products': products,
            'category': category,
            'price_min': price_min,
            'price_max': price_max,
            'rating': rating,
            'review': review,
            'sort': sort
        }
