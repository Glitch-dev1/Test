from django.urls import path

from .views import *

app_name = 'products'

urlpatterns = [
  path('', product_page, name= "product"),
  path('create/', productCreate, name= "createProduct"),
  path('<int:p_id>/', dynamic_products)
]