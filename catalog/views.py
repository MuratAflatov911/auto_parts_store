from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .models import Category, Product, VehicleEngine, VehicleGeneration, VehicleMake, VehicleModel


def catalog_list(request):
    qs = Product.objects.select_related('category').all()
    q = request.GET.get('q')
    if q:
        qs = qs.filter(Q(name__icontains=q) | Q(brand__icontains=q) | Q(article__icontains=q))
    if request.GET.get('category'):
        qs = qs.filter(category__slug=request.GET['category'])
    if request.GET.get('sort') == 'price':
        qs = qs.order_by('price')
    elif request.GET.get('sort') == '-price':
        qs = qs.order_by('-price')

    selected_engine = request.session.get('selected_engine_id')
    if selected_engine:
        qs = qs.filter(Q(compatible_engines=selected_engine) | Q(compatible_engines__isnull=True)).distinct()

    page = Paginator(qs.distinct(), 12).get_page(request.GET.get('page'))

    make_id = request.GET.get('make')
    model_id = request.GET.get('model')
    generation_id = request.GET.get('generation')
    context = {
        'page_obj': page,
        'categories': Category.objects.all(),
        'makes': VehicleMake.objects.all(),
        'models': VehicleModel.objects.filter(make_id=make_id) if make_id else VehicleModel.objects.none(),
        'generations': VehicleGeneration.objects.filter(model_id=model_id) if model_id else VehicleGeneration.objects.none(),
        'engines': VehicleEngine.objects.filter(generation_id=generation_id) if generation_id else VehicleEngine.objects.none(),
        'selected_make_id': make_id,
        'selected_model_id': model_id,
        'selected_generation_id': generation_id,
        'selected_engine_id': request.GET.get('engine', ''),
    }
    return render(request, 'catalog/list.html', context)


def product_detail(request, slug):
    p = get_object_or_404(Product, slug=slug)
    viewed = request.session.get('recently_viewed', [])
    if p.id not in viewed:
        viewed = [p.id] + viewed[:9]
    request.session['recently_viewed'] = viewed

    return render(request, 'catalog/detail.html', {
        'product': p,
        'similar': Product.objects.filter(category=p.category).exclude(id=p.id)[:4],
        'recently': Product.objects.filter(id__in=viewed)[:6],
    })


def vehicle_selector(request):
    if request.method == 'POST':
        engine_id = request.POST.get('engine')
        if not engine_id:
            messages.error(request, 'Выберите двигатель в списке.')
            return redirect(request.META.get('HTTP_REFERER', 'catalog:catalog_list'))
        engine = get_object_or_404(VehicleEngine, id=engine_id)
        request.session['selected_engine_id'] = engine.id
        request.session['selected_vehicle'] = (
            f'{engine.generation.model.make.name} {engine.generation.model.name} '
            f'{engine.generation.name} {engine.name}'
        )
        messages.success(request, 'Автомобиль выбран. Каталог отфильтрован.')
    return redirect(request.META.get('HTTP_REFERER', 'catalog:catalog_list'))


def clear_vehicle(request):
    request.session.pop('selected_engine_id', None)
    request.session.pop('selected_vehicle', None)
    messages.info(request, 'Фильтр автомобиля сброшен.')
    return redirect(request.META.get('HTTP_REFERER', 'catalog:catalog_list'))
