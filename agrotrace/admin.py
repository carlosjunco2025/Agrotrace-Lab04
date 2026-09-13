from django.contrib import admin
from .models import (
    CentroAcopio, VariedadCultivo, CertificacionAgricola,
    FundoProductor, LoteRecepcionado, EvaluacionCalidadLote, CertificacionLote
)

admin.site.register(CentroAcopio)
admin.site.register(VariedadCultivo)
admin.site.register(CertificacionAgricola)
admin.site.register(FundoProductor)
admin.site.register(LoteRecepcionado)
admin.site.register(EvaluacionCalidadLote)
admin.site.register(CertificacionLote)