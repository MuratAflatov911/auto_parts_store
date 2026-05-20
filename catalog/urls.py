from django.urls import path
from . import views
app_name='catalog'
urlpatterns=[path('',views.catalog_list,name='catalog_list'),path('vehicle/select/',views.vehicle_selector,name='vehicle_select'),path('vehicle/clear/',views.clear_vehicle,name='vehicle_clear'),path('<slug:slug>/',views.product_detail,name='product_detail')]
