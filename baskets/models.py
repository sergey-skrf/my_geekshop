from django.db import models

from users.models import User
from products.models import Product

# Create your models here.
class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def cost(self):
        return self.quantity * self.product.price

    def total_quantity(self):
        result = 0
        for item in Basket.objects.values('quantity'):
            result += item['quantity']
        return result

    def total_sum(self):
        result = 0
        quantity_list = Basket.objects.values('quantity')
        product_price_list = Basket.objects.values('product__price')
        i = 0
        while i < len(quantity_list):
            result += (quantity_list[i]['quantity'] * product_price_list[i]['product__price'])
            i += 1
        return result