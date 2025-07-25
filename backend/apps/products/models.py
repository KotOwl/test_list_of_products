from core.models import BaseModel
from django.db import models


class ProductModel(BaseModel):
    class Meta:
        db_table ="products"

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)


class ProductImageModel(BaseModel):
    class Meta:
        db_table = 'images'

    image_of_product = models.ImageField(upload_to='upload_advertisement_photo',blank=True)
    product = models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE,
        related_name='images',
        blank=True
    )
