from django.conf import settings
from django.db import models
from catalog.models import Product
class Order(models.Model):
    STATUS=(('new','Новый'),('processing','В обработке'),('done','Завершён'))
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=150); phone=models.CharField(max_length=20); address=models.CharField(max_length=255)
    city=models.CharField(max_length=100); comment=models.TextField(blank=True); created_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=20,choices=STATUS,default='new')
class OrderItem(models.Model): order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items'); product=models.ForeignKey(Product,on_delete=models.CASCADE); quantity=models.PositiveIntegerField(default=1); price=models.DecimalField(max_digits=10,decimal_places=2)
