

from logger import log_api
from product.models import Product
from typing import List, Optional


def filter_products(
    category: Optional[str] = None,
    price_min: Optional[str] = None,
    price_max: Optional[str] = None,
    rating: Optional[str] = None,
    review: Optional[str] = None,
    sort: Optional[str] = None) -> List[Product]:

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

    if sort:
            products = products.order_by(sort)
    
    return products