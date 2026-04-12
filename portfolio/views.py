from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from .models import Asset, Dividend
from .forms import AssetForm


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
            asset = form.save(commit=False)
            asset.user = request.user
            asset.save()
            messages.success(request, 'Asset added successfully!')
            return redirect('asset_list')
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