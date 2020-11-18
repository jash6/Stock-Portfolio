from django import forms
from .models import Stock


class StockForm(forms.ModelForm):
    ticker = forms.CharField()
    class Meta:
        model= Stock
        fields= ('ticker',)