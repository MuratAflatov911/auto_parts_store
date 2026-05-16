def selected_vehicle(request):
    return {'selected_vehicle':request.session.get('selected_vehicle')}
