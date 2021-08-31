from django.urls import path
from .views import item_list, checkout, product

app_name = 'core'

urlpatterns = [
    path('', item_list, name='home'),
    path('product/', product, name='product'),
    path('checkout/', checkout, name='checkout'),
]