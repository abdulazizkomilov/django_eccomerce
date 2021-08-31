from django.shortcuts import render
from .models import Item
from django.views.generic import View

def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'home.html', context)

def product(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'product.html', context)

def checkout(request):
    return render(request, "checkout.html")
