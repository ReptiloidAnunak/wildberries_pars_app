from django.db import models




class Product(models.Model):
    class Meta:
        db_table = 'product'
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
    
    title = models.CharField(max_length=5000, verbose_name="Название")
    price_original = models.FloatField(verbose_name='Цена')
    price = models.FloatField(verbose_name='Цена co скидкой')
    rating = models.IntegerField(verbose_name='Рейтинг')
    review_amount = models.IntegerField(verbose_name='Количество отзывов')