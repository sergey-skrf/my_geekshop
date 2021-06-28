from django.shortcuts import render

# Create your views here.
# функции = контролеры = вьюхи

def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals',
             'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
             'price': 6090},
            {'name': 'Синяя куртка The North Face',
             'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
             'price': 23725},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
             'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
             'price': 3390},
            {'name': 'Черный рюкзак Nike Heritage',
             'description': 'Плотная ткань. Легкий материал.',
             'price': 2340},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
             'description': 'Гладкий кожаный верх. Натуральный материал.',
             'price': 13590},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
             'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
             'price': 2890},
        ],
    }
    return render(request, 'products/products.html', context)

