from django.urls import path
from .views import (
    HomeView, checkout,
    ItemDetailView, add_to_card,
    remove_from_cart,
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('checkout/', checkout, name='checkout'),
    path('add-to-card/<slug>', add_to_card, name='add-to-card'),
    path('remove-from-card/<slug>', remove_from_cart, name='remove_from_cart'),
]