import os
import json

from django.shortcuts import render
from products.models import ProductCategory, Product

MODULE_DIR = os.path.dirname(__file__)

# Create your views here.
# функции = контролеры = вьюхи

def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {'title': 'GeekShop - Каталог',
               'products': Product.objects.all(),
               'category': ProductCategory.objects.all()
               }
    #file_path = os.path.join(MODULE_DIR, "fixtures/goods.json")
    #context['products'] = json.load(open(file_path, encoding='utf-8'))
    return render(request, 'products/products.html', context)
