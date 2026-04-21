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
                'placeholder': 'e.g. PETR4',
                'maxlength': '10',
                'autocomplete': 'off',
            }),
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
        }


class DividendForm(forms.ModelForm):
    class Meta:
        model = Dividend
        fields = ['asset', 'value', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['asset'].queryset = Asset.objects.filter(user=user)