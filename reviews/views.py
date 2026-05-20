from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .forms import ReviewForm
from catalog.models import Product
@login_required
def add_review(request,product_id):
    p=get_object_or_404(Product,id=product_id)
    f=ReviewForm(request.POST)
    if f.is_valid():
        r=f.save(commit=False); r.user=request.user; r.product=p; r.save()
    return redirect(p.get_absolute_url())
