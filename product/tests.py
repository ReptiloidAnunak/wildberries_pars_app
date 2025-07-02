from django.test import TestCase
from product.models import Product

class ProductModelTest(TestCase):
    def setUp(self):
        Product.objects.create(
            name="Test Product",
            price=100.0,
            category="Test Category",
            rating=4.5,
            review_count=10
        )

    def test_product_creation(self):
        product = Product.objects.get(name="Test Product")
        self.assertEqual(product.price, 100.0)
        self.assertEqual(product.category, "Test Category")
        self.assertEqual(product.rating, 4.5)
        self.assertEqual(product.review_count, 10)
