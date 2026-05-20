from .models import VehicleEngine, VehicleGeneration, VehicleMake, VehicleModel


def selected_vehicle(request):
    is_catalog = request.path.startswith('/catalog')
    make_id = request.GET.get('make') if is_catalog else None
    model_id = request.GET.get('model') if is_catalog else None
    generation_id = request.GET.get('generation') if is_catalog else None
    return {
        'selected_vehicle': request.session.get('selected_vehicle'),
        'show_vehicle_filter': is_catalog,
        'makes': VehicleMake.objects.all() if is_catalog else VehicleMake.objects.none(),
        'models': VehicleModel.objects.filter(make_id=make_id) if make_id else VehicleModel.objects.none(),
        'generations': VehicleGeneration.objects.filter(model_id=model_id) if model_id else VehicleGeneration.objects.none(),
        'engines': VehicleEngine.objects.filter(generation_id=generation_id) if generation_id else VehicleEngine.objects.none(),
    }
