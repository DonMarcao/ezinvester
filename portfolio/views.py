from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from .models import Asset, Dividend
from .forms import AssetForm, DividendForm


@login_required
def dashboard(request):
    assets = Asset.objects.filter(user=request.user)

    # Type Filter
    asset_type = request.GET.get('type')
    if asset_type:
        assets = assets.filter(asset_type=asset_type.upper())

    total_invested = sum(a.total_value() for a in assets)
    asset_count = assets.count()
    total_dividends = Dividend.objects.filter(
        asset__user=request.user
    ).aggregate(total=Sum('value'))['total'] or 0

    # Gráfico 1 — por asset individual
    chart_labels = [a.ticker for a in assets]
    chart_data = [float(a.total_value()) for a in assets]

    # Gráfico 2 — por tipo de asset
    type_totals = {}
    for a in assets:
        type_totals[a.asset_type] = type_totals.get(a.asset_type, 0) + float(a.total_value())
    chart_type_labels = list(type_totals.keys())
    chart_type_data = list(type_totals.values())

    context = {
        'assets': assets,
        'total_invested': total_invested,
        'asset_count': asset_count,
        'total_dividends': total_dividends,
        'chart_labels': chart_labels,
        'chart_data': chart_data,
        'chart_type_labels': chart_type_labels,
        'chart_type_data': chart_type_data,
        'selected_type': asset_type or '',
    }
    return render(request, 'portfolio/dashboard.html', context)

@login_required
def asset_list(request):
    assets = Asset.objects.filter(user=request.user)
    asset_type = request.GET.get('type')
    if asset_type:
        assets = assets.filter(asset_type=asset_type)
    return render(request, 'portfolio/asset_list.html', {'assets': assets})


@login_required
def asset_add(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            ticker = form.cleaned_data['ticker'].upper()
            try:
                import yfinance as yf
                ticker_data = yf.Ticker(ticker)
                info = ticker_data.fast_info
                # fast_info raises exception or returns empty for invalid tickers
                market_price = getattr(info, 'last_price', None)
                if market_price is None:
                    form.add_error('ticker', 'Invalid ticker. Please check and try again.')
                    return render(request, 'portfolio/asset_form.html', {
                        'form': form, 'title': 'Add Asset'
                    })
                asset = form.save(commit=False)
                asset.ticker = ticker
                asset.user = request.user
                if not asset.name:
                    try:
                        full_info = ticker_data.info
                        asset.name = full_info.get('longName') or full_info.get('shortName') or ticker
                    except Exception:
                        asset.name = ticker
                asset.save()
                messages.success(request, 'Asset added successfully!')
                return redirect('asset_list')
            except Exception:
                form.add_error('ticker', 'Invalid ticker. Please check and try again.')
                return render(request, 'portfolio/asset_form.html', {
                    'form': form, 'title': 'Add Asset'
                })
    else:
        form = AssetForm()
    return render(request, 'portfolio/asset_form.html', {
        'form': form, 'title': 'Add Asset'
    })


@login_required
def asset_edit(request, pk):
    asset = get_object_or_404(Asset, pk=pk, user=request.user)
    if request.method == 'POST':
        form = AssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Asset updated successfully!')
            return redirect('asset_list')
    else:
        form = AssetForm(instance=asset)
    return render(request, 'portfolio/asset_form.html', {
        'form': form, 'title': 'Edit Asset'
    })


@login_required
def asset_delete(request, pk):
    asset = get_object_or_404(Asset, pk=pk, user=request.user)
    if request.method == 'POST':
        asset.delete()
        messages.success(request, 'Asset deleted successfully!')
        return redirect('asset_list')
    return render(request, 'portfolio/asset_confirm_delete.html', {
        'asset': asset
    })

@login_required
def dividend_list(request):
    dividends = Dividend.objects.filter(asset__user=request.user)
    total_dividends = dividends.aggregate(
        total=Sum('value'))['total'] or 0
    return render(request, 'portfolio/dividend_list.html', {
        'dividends': dividends,
        'total_dividends': total_dividends,
    })


@login_required
def dividend_add(request):
    if request.method == 'POST':
        form = DividendForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dividend added successfully!')
            return redirect('dividend_list')
    else:
        form = DividendForm(request.user)
    return render(request, 'portfolio/dividend_form.html', {
        'form': form, 'title': 'Add Dividend'
    })


@login_required
def dividend_edit(request, pk):
    dividend = get_object_or_404(
        Dividend, pk=pk, asset__user=request.user
    )
    if request.method == 'POST':
        form = DividendForm(request.user, request.POST, instance=dividend)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dividend updated successfully!')
            return redirect('dividend_list')
    else:
        form = DividendForm(request.user, instance=dividend)
    return render(request, 'portfolio/dividend_form.html', {
        'form': form, 'title': 'Edit Dividend'
    })


@login_required
def dividend_delete(request, pk):
    dividend = get_object_or_404(
        Dividend, pk=pk, asset__user=request.user
    )
    if request.method == 'POST':
        dividend.delete()
        messages.success(request, 'Dividend deleted successfully!')
        return redirect('dividend_list')
    return render(request, 'portfolio/dividend_confirm_delete.html', {
        'dividend': dividend
    })