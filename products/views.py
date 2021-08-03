import os
import json

from django.shortcuts import render
from products.models import ProductCategory, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

MODULE_DIR = os.path.dirname(__file__)

# Create your views here.
# функции = контролеры = вьюхи

def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'products/index.html', context)

def products(request, category_id=None, page=1):
    context = {'title': 'GeekShop - Каталог', 'category': ProductCategory.objects.all()}
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
        paginator = Paginator(products, 3)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)
    context['products'] = products_paginator

    #file_path = os.path.join(MODULE_DIR, "fixtures/goods.json")
    #context['products'] = json.load(open(file_path, encoding='utf-8'))
    return render(request, 'products/products.html', context)
