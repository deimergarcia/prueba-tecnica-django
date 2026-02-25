from django import forms
from .models import Cliente, Oportunidad

class ClienteForm(forms.ModelForm):
    ciudad = forms.ChoiceField(choices=[], required=False, widget=forms.Select(attrs={'class': 'form-control'}))

    def __init__(self, *args, ciudades=None, **kwargs):
        super().__init__(*args, **kwargs)
        if ciudades:
            choices = [('', '---------')] + [(c, c) for c in ciudades]
            self.fields['ciudad'].choices = choices
        else:
            self.fields['ciudad'].widget = forms.TextInput(attrs={'class': 'form-control'})
            self.fields['ciudad'].help_text = "La API no está disponible. Ingrese manualmente."

        if self.instance and self.instance.pk and self.instance.ciudad:
            self.fields['ciudad'].initial = self.instance.ciudad

    class Meta:
        model = Cliente
        fields = ['nombre_completo', 'empresa', 'correo', 'telefono', 'ciudad']
        widgets = {
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }

class OportunidadForm(forms.ModelForm):
    class Meta:
        model = Oportunidad
        fields = ['cliente', 'descripcion', 'valor_estimado', 'estado']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'valor_estimado': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }