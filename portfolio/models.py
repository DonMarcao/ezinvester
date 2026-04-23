from django.db import models
from django.contrib.auth.models import User


class Asset(models.Model):
    ASSET_TYPES = [
        ('STOCK', 'Stock'),
        ('ETF', 'ETF'),
        ('REIT', 'REIT'),
        ('CRYPTO', 'Crypto'),
        ('TREASURY', 'Treasury'),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='assets'
    )
    ticker = models.CharField(max_length=20)
    name = models.CharField(max_length=100, blank=True)
    shares = models.DecimalField(max_digits=10, decimal_places=4)
    average_price = models.DecimalField(max_digits=10, decimal_places=2)
    asset_type = models.CharField(max_length=10, choices=ASSET_TYPES)
    purchase_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def total_value(self):
        return self.shares * self.average_price

    def __str__(self):
        return f"{self.ticker} ({self.user.username})"


class Dividend(models.Model):
    asset = models.ForeignKey(
        Asset, on_delete=models.CASCADE, related_name='dividends'
    )
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.asset.ticker} - {self.value} ({self.date})"
