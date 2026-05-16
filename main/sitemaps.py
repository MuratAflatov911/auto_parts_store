from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from catalog.models import Product
class StaticViewSitemap(Sitemap):
    def items(self): return ['main:home','main:about','main:contacts','catalog:catalog_list']
    def location(self,item): return reverse(item)
class ProductSitemap(Sitemap):
    def items(self): return Product.objects.all()
