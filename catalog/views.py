from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .models import Category, Product, VehicleMake, VehicleModel, VehicleGeneration, VehicleEngine

def catalog_list(request):
    qs=Product.objects.select_related('category').all()
    q=request.GET.get('q')
    if q: qs=qs.filter(Q(name__icontains=q)|Q(brand__icontains=q)|Q(article__icontains=q))
    if request.GET.get('category'): qs=qs.filter(category__slug=request.GET['category'])
    if request.GET.get('sort')=='price': qs=qs.order_by('price')
    elif request.GET.get('sort')=='-price': qs=qs.order_by('-price')
    if request.session.get('selected_engine_id'): qs=qs.filter(compatible_engines=request.session['selected_engine_id'])|qs.filter(compatible_engines__isnull=True)
    page=Paginator(qs.distinct(),12).get_page(request.GET.get('page'))
    return render(request,'catalog/list.html',{'page_obj':page,'categories':Category.objects.all()})

def product_detail(request,slug):
    p=get_object_or_404(Product,slug=slug)
    viewed=request.session.get('recently_viewed',[])
    if p.id not in viewed: viewed=[p.id]+viewed[:9]
    request.session['recently_viewed']=viewed
    return render(request,'catalog/detail.html',{'product':p,'similar':Product.objects.filter(category=p.category).exclude(id=p.id)[:4],'recently':Product.objects.filter(id__in=viewed)[:6]})

def vehicle_selector(request):
    if request.method=='POST':
        engine=get_object_or_404(VehicleEngine,id=request.POST.get('engine'))
        request.session['selected_engine_id']=engine.id
        request.session['selected_vehicle']=f"{engine.generation.model.make.name} {engine.generation.model.name} {engine.generation.name} {engine.name}"
        messages.success(request,'Автомобиль выбран')
    return redirect(request.META.get('HTTP_REFERER','main:home'))

def clear_vehicle(request):
    request.session.pop('selected_engine_id',None); request.session.pop('selected_vehicle',None)
    return redirect(request.META.get('HTTP_REFERER','main:home'))
