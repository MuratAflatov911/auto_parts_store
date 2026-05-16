from django.urls import path
from . import views
app_name='main'
urlpatterns=[path('',views.home,name='home'),path('about/',views.about,name='about'),path('contacts/',views.contacts,name='contacts'),path('news/',views.news,name='news'),path('promotions/',views.promotions,name='promotions'),path('robots.txt',lambda r: __import__('django.http').http.HttpResponse('User-agent: *\nAllow: /\nSitemap: /sitemap.xml',content_type='text/plain'))]
