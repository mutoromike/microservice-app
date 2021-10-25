"""products URL Configuration
"""

from django.contrib import admin
from django.urls import path

from .views import ProductViewSet

urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get': 'list_products',
        'post': 'create'
    })),
    path('products/<str:pk>', ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]
