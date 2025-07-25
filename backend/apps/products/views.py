from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView

from apps.products.models import ProductModel
from apps.products.serializer import ProductSerializer


class ProductListApiView(ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class =ProductSerializer

class CreateProductApiView(CreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

class ProductDetailApiView(RetrieveUpdateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'