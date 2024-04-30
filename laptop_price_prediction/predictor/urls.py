from django.urls import path
from .views import predict_laptop_price

urlpatterns = [
    path('', predict_laptop_price, name='predict_laptop_price'),
]
