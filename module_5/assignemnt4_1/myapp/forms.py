from django import forms
from .models import ProductSubCat

class ProductSubCatForm(forms.ModelForm):
    class Meta:
        model = ProductSubCat
        fields = ['product_price', 'product_image', 'product_model', 'product_ram']


class ProductSearchForm(forms.Form):
    q = forms.CharField(label='Search', max_length=255, required=False)

