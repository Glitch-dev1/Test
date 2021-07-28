from django.shortcuts import render

from products.models import Product

def home_page(request):
    
    context = {
        "product": Product
    }
    return render(request, 'base.html', context)
   
def report(request, id):
    try:
        emp_item = Product.objects.get(id=id)
        return render(request, 'base.html', {'prd':emp_item})
    except Employee.DoesNotExist:
        return render(request, 'base.html', {'error': 'No data found.'})
    
def create_product(request):
    
    context = {
        
    }
    return render(request, 'create.html', context)