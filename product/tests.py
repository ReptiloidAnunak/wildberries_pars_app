from django.test import TestCase
from logger import log_api
from product.models import Product
from wb_pars_api_server.settings import WB_SEARCH_URL
from parsers.wb_parser import get_wb_products
import random

PRICE_ORIGINAL = 1000.0  # Example price for the product
PRICE = 900.0
RATING = 5
REVIEW_COUNT = 10

class ProductModelTest(TestCase):
    
    def setUp(self):
        Product.objects.create(
            title="Test Product",
            price_original=PRICE_ORIGINAL,
            price=900.0,
            rating=5,
            review_amount=10
        )

    def test_product_creation(self):
        try:
            product = Product.objects.get(title="Test Product")
            self.assertEqual(product.price, PRICE)
            self.assertEqual(product.rating, RATING)
            self.assertEqual(product.review_amount, REVIEW_COUNT)
            log_api.info(f"✅ TEST : Product created: {product.title} with price {product.price}")
        except Exception as e:
            log_api.error(f"❌ TEST : test_product_creation: {e}", exc_info=True)
            raise



class ProductViewTest(TestCase):
    
    def setUp(self):
        Product.objects.create(
            title="Test Product",
            price_original=PRICE_ORIGINAL,
            price=PRICE,
            rating=RATING,
            review_amount=REVIEW_COUNT
        )

    def test_product_view(self):
        try:
            response = self.client.get('/api/products/')
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, "Test Product")
            log_api.info("✅ TEST : Product view returned successfully")
        except Exception as e:
            log_api.error(f"❌ TEST : test_product_view: {e}", exc_info=True)
            raise

    def test_get_wb_products(self):
        page_prods_amount = 100
        category = random.choice(['ваза', 'стул', 'стол', 'ящик', 'духи', 'паяльник'])
        try:
            wb_products = get_wb_products(category, page=1)
            wb_products_amount = len(wb_products)
            self.assertTrue(wb_products_amount > 0)
            log_api.info(f"\n✅ TEST : get_wb_products({category})\nwb_products_amount: {wb_products_amount}")
        except Exception as e:
            log_api.error(f"❌ TEST : get_wb_products({category})", exc_info=True)
            raise

    def test_admin_login_view(self):
        try:
            response = self.client.get('/admin/login/?next=/admin/')
            self.assertEqual(response.status_code, 200)
            log_api.info("✅ TEST : Admin login view returned successfully")
        except Exception as e:
            log_api.error(f"❌ TEST : test_admin_login_view: {e}", exc_info=True)
            raise