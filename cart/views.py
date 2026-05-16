from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Cart, CartItem
from catalog.models import Product
@login_required
def cart_detail(request):
    cart,_=Cart.objects.get_or_create(user=request.user)
    return render(request,'cart/detail.html',{'cart':cart})
@login_required
def add_to_cart(request,product_id):
    cart,_=Cart.objects.get_or_create(user=request.user); p=get_object_or_404(Product,id=product_id)
    item,_=CartItem.objects.get_or_create(cart=cart,product=p); item.quantity+=1; item.save(); return redirect('cart:detail')
