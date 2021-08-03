from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs = {
             "rows": "10",
             "cols": "35",
         }
      )
   )
        
    class Meta:
        model  = Product
        fields = [
            'name',
            'price',
            'description',
            'image',
        ]