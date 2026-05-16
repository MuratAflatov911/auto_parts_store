from .models import VehicleGeneration, VehicleMake, VehicleModel, VehicleEngine


def selected_vehicle(request):
    make_id = request.GET.get('make')
    model_id = request.GET.get('model')
    generation_id = request.GET.get('generation')
    return {
        'selected_vehicle': request.session.get('selected_vehicle'),
        'makes': VehicleMake.objects.all(),
        'models': VehicleModel.objects.filter(make_id=make_id) if make_id else VehicleModel.objects.none(),
        'generations': VehicleGeneration.objects.filter(model_id=model_id) if model_id else VehicleGeneration.objects.none(),
        'engines': VehicleEngine.objects.filter(generation_id=generation_id) if generation_id else VehicleEngine.objects.none(),
    }
