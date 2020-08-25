from django import forms
from .models import Inventory
class InventoryForm(forms.ModelForm):
    class Meta:
        model=Inventory
        fields={'title','csv_file','date'}
