from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Asset, Dividend


@login_required
def dashboard(request):
    assets = Asset.objects.filter(user=request.user)
    total_invested = sum(a.total_value() for a in assets)
    asset_count = assets.count()
    total_dividends = Dividend.objects.filter(
        asset__user=request.user
    ).aggregate(total=Sum('value'))['total'] or 0

    context = {
        'assets': assets,
        'total_invested': total_invested,
        'asset_count': asset_count,
        'total_dividends': total_dividends,
    }
    return render(request, 'portfolio/dashboard.html', context)