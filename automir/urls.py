from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from main.sitemaps import StaticViewSitemap, ProductSitemap
sitemaps = {'static': StaticViewSitemap, 'products': ProductSitemap}
handler404='main.views.handler404'; handler500='main.views.handler500'
urlpatterns=[
    path('admin/',admin.site.urls),
    path('',include('main.urls')),
    path('catalog/',include('catalog.urls')),
    path('accounts/',include('accounts.urls')),
    path('cart/',include('cart.urls')),
    path('orders/',include('orders.urls')),
    path('reviews/',include('reviews.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Администрирование Автомир'
admin.site.site_title = 'Автомир Админка'
admin.site.index_title = 'Управление магазином'
