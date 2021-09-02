from django.urls import path
from .views import (
    HomeView, CheckoutView,
    ItemDetailView, add_to_card,
    remove_from_cart, OrderSummaryView,
    remove_single_item_from_cart,
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('add-to-card/<slug>', add_to_card, name='add-to-card'),
    path('remove-from-card/<slug>', remove_from_cart, name='remove_from_cart'),
    path('remove-item-from-cart/<slug>', remove_single_item_from_cart, name='remove-single-item-from-cart'),
]