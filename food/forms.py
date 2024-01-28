from django import forms
from .models import Items


class ItemsForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['items_name', 'items_desc', 'items_price',
                  'items_image',]
