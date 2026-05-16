from django.conf import settings
from django.db import models
from catalog.models import Product
class Review(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='reviews')
    text=models.TextField(); rating=models.PositiveSmallIntegerField(default=5); created_at=models.DateTimeField(auto_now_add=True)
