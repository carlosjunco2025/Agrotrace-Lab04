from django import forms
from .models import FundoProductor, LoteRecepcionado
from .models import FundoProductor, LoteRecepcionado, CertificacionLote

class FundoProductorForm(forms.ModelForm):
    class Meta:
        model = FundoProductor
        fields = ['nombre_fundo', 'propietario_dni_ruc', 'hectareas', 'valido_exportacion']
        widgets = {
            'nombre_fundo': forms.TextInput(attrs={'class': 'form-control'}),
            'propietario_dni_ruc': forms.TextInput(attrs={'class': 'form-control'}),
            'hectareas': forms.NumberInput(attrs={'class': 'form-control'}),
            'valido_exportacion': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class LoteRecepcionadoForm(forms.ModelForm):
    class Meta:
        model = LoteRecepcionado
        fields = ['fundo', 'codigo_lote', 'toneladas_brutas', 'porcentaje_descarte', 'estado_evaluacion']
        widgets = {
            'fundo': forms.Select(attrs={'class': 'form-select'}),
            'codigo_lote': forms.TextInput(attrs={'class': 'form-control'}),
            'toneladas_brutas': forms.NumberInput(attrs={'class': 'form-control'}),
            'porcentaje_descarte': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado_evaluacion': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CertificacionLoteForm(forms.ModelForm):
    class Meta:
        model = CertificacionLote
        fields = ['lote', 'certificacion', 'fecha_auditoria', 'codigo_inspeccion']
        widgets = {
            'lote': forms.Select(attrs={'class': 'form-select'}),
            'certificacion': forms.Select(attrs={'class': 'form-select'}),
            'fecha_auditoria': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'codigo_inspeccion': forms.TextInput(attrs={'class': 'form-control'}),
        }