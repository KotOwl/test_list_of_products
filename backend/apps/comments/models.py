from apps.products.models import ProductModel
from core.models import BaseModel
from django.db import models


class CommentModel(BaseModel):
    class Meta:
        db_table="comments"

    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=600)
