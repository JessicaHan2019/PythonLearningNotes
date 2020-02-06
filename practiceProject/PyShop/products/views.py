from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):
    products = Product.objects.all()  # returns all the products we have in the database
    # Product.objects.filter/get/save ()
    return render(request, 'index.html',
                  {'products': products})  # we use this function to render a template


def new_product(request):
    return  HttpResponse('New Product')
