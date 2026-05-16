from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import RegisterForm
from orders.models import Order

def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            u=form.save(); login(request,u); return redirect('main:home')
    else: form=RegisterForm()
    return render(request,'accounts/register.html',{'form':form})
@login_required
def profile(request): return render(request,'accounts/profile.html',{'orders':Order.objects.filter(user=request.user)})
