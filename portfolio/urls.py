from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('assets/', views.asset_list, name='asset_list'),
    path('assets/add/', views.asset_add, name='asset_add'),
    path('assets/<int:pk>/edit/', views.asset_edit, name='asset_edit'),
    path('assets/<int:pk>/delete/', views.asset_delete, name='asset_delete'),
]