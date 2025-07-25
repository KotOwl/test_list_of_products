from rest_framework.serializers import ModelSerializer

from apps.products.models import ProductModel, ProductImageModel


class ProductSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ('id','price','description','name','created_at', 'updated_at')
        read_only_fields=('id','created_at', 'updated_at' )


class ProductImageSerializer(ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model =ProductImageModel
        fields = ('id', 'image_of_product','product', 'created_at', 'updated_at')
        read_only_fields = ('id', 'product','created_at', 'updated_at')