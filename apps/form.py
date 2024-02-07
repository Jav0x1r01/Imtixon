from django import forms

from apps.models import UserModel


class ProductForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('title', 'price', 'old_price', 'sale','image')
        # exclude = ('created_at',)
