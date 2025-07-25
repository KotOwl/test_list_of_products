from rest_framework.urls import path

from apps.products.views import ProductListApiView, CreateProductApiView, ProductDetailApiView

urlpatterns = [
    path('/get',ProductListApiView.as_view()),
    path('/create',CreateProductApiView.as_view()),
    path('/<int:pk>',ProductDetailApiView.as_view())
]