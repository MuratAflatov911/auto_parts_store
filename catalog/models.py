from django.db import models
from django.urls import reverse

class VehicleMake(models.Model): name=models.CharField(max_length=100)
class VehicleModel(models.Model): make=models.ForeignKey(VehicleMake,on_delete=models.CASCADE,related_name='models'); name=models.CharField(max_length=100)
class VehicleGeneration(models.Model): model=models.ForeignKey(VehicleModel,on_delete=models.CASCADE,related_name='generations'); name=models.CharField(max_length=100)
class VehicleEngine(models.Model): generation=models.ForeignKey(VehicleGeneration,on_delete=models.CASCADE,related_name='engines'); name=models.CharField(max_length=120); year_from=models.PositiveIntegerField(); year_to=models.PositiveIntegerField(null=True,blank=True); volume=models.CharField(max_length=20,blank=True)
class Category(models.Model):
    name=models.CharField(max_length=120); slug=models.SlugField(unique=True); image=models.ImageField(upload_to='categories/',blank=True,null=True)
    def __str__(self): return self.name
class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    compatible_engines=models.ManyToManyField(VehicleEngine,blank=True,related_name='products')
    name=models.CharField(max_length=220); slug=models.SlugField(unique=True); description=models.TextField(); price=models.DecimalField(max_digits=10,decimal_places=2)
    old_price=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True); stock=models.PositiveIntegerField(default=0)
    article=models.CharField(max_length=50); brand=models.CharField(max_length=80); image=models.ImageField(upload_to='products/',blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True); is_popular=models.BooleanField(default=False)
    def __str__(self): return self.name
    def get_absolute_url(self): return reverse('catalog:product_detail',args=[self.slug])
class ProductImage(models.Model): product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='images'); image=models.ImageField(upload_to='products/gallery/')
class News(models.Model): title=models.CharField(max_length=180); content=models.TextField(); image=models.ImageField(upload_to='news/',blank=True,null=True); created_at=models.DateTimeField(auto_now_add=True)
class Discount(models.Model): title=models.CharField(max_length=180); description=models.TextField(); percent=models.PositiveIntegerField(); active=models.BooleanField(default=True)
