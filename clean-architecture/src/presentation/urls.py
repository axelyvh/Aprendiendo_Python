from django.urls import path
from src.presentation.views import ProductView

urlpatterns = [
    path('detail/', ProductView.as_view(), name='product-detail'),
]