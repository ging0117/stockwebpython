from django import forms
from .models import Stock

class addStockForm(forms.ModelForm):
    class Meta:
        model=Stock
        fields=('symbol','qty')
