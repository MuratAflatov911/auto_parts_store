from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from catalog.models import Product
from .models import Cart, CartItem


@login_required
def cart_detail(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    total = sum(item.product.price * item.quantity for item in cart.items.select_related('product').all())
    return render(request, 'cart/detail.html', {'cart': cart, 'total': total})


@login_required
def add_to_cart(request, product_id):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product, defaults={'quantity': 1})
    if not created:
        item.quantity += 1
        item.save(update_fields=['quantity'])
    messages.success(request, f'Товар «{product.name}» добавлен в корзину.')
    return redirect('cart:detail')


@login_required
def update_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    qty = int(request.POST.get('quantity', 1))
    if qty <= 0:
        item.delete()
        messages.info(request, 'Товар удалён из корзины.')
    else:
        item.quantity = qty
        item.save(update_fields=['quantity'])
        messages.success(request, 'Количество товара обновлено.')
    return redirect('cart:detail')


@login_required
def remove_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()
    messages.info(request, 'Товар удалён из корзины.')
    return redirect('cart:detail')
