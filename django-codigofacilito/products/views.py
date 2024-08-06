from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    # Logica
    products = Product.objects.all()
    return render(request, 'list_of_products.html', {'products': products})