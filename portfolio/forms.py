from django import forms
from .models import Asset, Dividend


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = [
            'ticker', 'name', 'shares',
            'average_price', 'asset_type', 'purchase_date'
        ]
        widgets = {
            'ticker': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. PETR4',
                'maxlength': '10',
                'autocomplete': 'off',
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'shares': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'average_price': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'asset_type': forms.Select(attrs={
                'class': 'form-select',
            }),
            'purchase_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
        }


class DividendForm(forms.ModelForm):
    class Meta:
        model = Dividend
        fields = ['asset', 'value', 'date']
        widgets = {
            'asset': forms.Select(attrs={
                'class': 'form-select',
            }),
            'value': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['asset'].queryset = Asset.objects.filter(user=user)