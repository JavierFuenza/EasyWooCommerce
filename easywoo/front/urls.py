from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.getProductos, name='getProductos'),
    path('home/', views.home, name='home'),
]
