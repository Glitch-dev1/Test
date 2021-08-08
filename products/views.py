from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

from .models import Product
from .forms import ProductForm
# Create your views here.
def productCreate(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/product")
    
    context = {
        "form" : form
    }
    return render(request, 'products/create.html', context)
  
def product_page(request):
    obj = Product.objects.all()
    
    context = {
        "prd": obj
    }
    return render(request, 'products/all_products.html', context)
    
def dynamic_products(request, p_id):
    obj = Product.objects.get(id=p_id)
    try:
        p_id= Product.objects.get(id=p_id)
    except Product.DoesNotExist:
        raise Http404
        
    context = {
        "prd": obj
    }
    return render(request, 'products/dynamic_look.html', context)