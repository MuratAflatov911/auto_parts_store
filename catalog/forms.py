from django import forms
from .models import VehicleMake, VehicleModel, VehicleGeneration, VehicleEngine


class VehicleSelectForm(forms.Form):
    make = forms.ModelChoiceField(queryset=VehicleMake.objects.all(), required=False)
    model = forms.ModelChoiceField(queryset=VehicleModel.objects.none(), required=False)
    generation = forms.ModelChoiceField(queryset=VehicleGeneration.objects.none(), required=False)
    engine = forms.ModelChoiceField(queryset=VehicleEngine.objects.none(), required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['make'].widget.attrs.update({'class': 'form-select'})
        self.fields['model'].widget.attrs.update({'class': 'form-select'})
        self.fields['generation'].widget.attrs.update({'class': 'form-select'})
        self.fields['engine'].widget.attrs.update({'class': 'form-select'})
