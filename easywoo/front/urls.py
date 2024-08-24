from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('producto/<int:id>/', views.product, name='product'),
]
