from django.shortcuts import render
from catalog.models import Category, Discount, News, Product


def home(request):
    return render(request, 'main/home.html', {
        'popular_products': Product.objects.filter(is_popular=True)[:8],
        'categories': Category.objects.all()[:8],
        'discounts': Discount.objects.filter(active=True)[:3],
    })


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def news(request):
    return render(request, 'main/news.html', {'news_list': News.objects.all()[:20]})


def promotions(request):
    return render(request, 'main/promotions.html', {'discounts': Discount.objects.filter(active=True)})


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
