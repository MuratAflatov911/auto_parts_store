from django.urls import path
from django.contrib.auth import views as auth
from . import views
app_name='accounts'
urlpatterns=[path('register/',views.register,name='register'),path('login/',auth.LoginView.as_view(template_name='accounts/login.html'),name='login'),path('logout/',auth.LogoutView.as_view(),name='logout'),path('profile/',views.profile,name='profile')]
