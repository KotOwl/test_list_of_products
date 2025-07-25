from rest_framework import serializers

from apps.comments.models import CommentModel
from apps.products.serializer import ProductSerializer


class CommentSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CommentModel
        fields = ('id', 'text', 'created_at', 'product', 'updated_at')
        read_only_fields = ('id', 'created_at', 'product', 'updated_at')
