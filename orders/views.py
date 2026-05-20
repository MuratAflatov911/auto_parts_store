from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import OrderForm
from .models import Order, OrderItem
from cart.models import Cart
@login_required
def checkout(request):
    cart=getattr(request.user,'cart',None)
    if not cart or not cart.items.exists(): return redirect('cart:detail')
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            order=form.save(commit=False); order.user=request.user; order.save()
            for i in cart.items.all(): OrderItem.objects.create(order=order,product=i.product,quantity=i.quantity,price=i.product.price)
            cart.items.all().delete(); messages.success(request,'Заказ успешно оформлен!'); return redirect('accounts:profile')
    else: form=OrderForm()
    return render(request,'orders/checkout.html',{'form':form,'cart':cart})
