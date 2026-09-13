from django.db import models


class CentroAcopio(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre


class VariedadCultivo(models.Model):
    nombre_cultivo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_cultivo


class CertificacionAgricola(models.Model):
    nombre_certificacion = models.CharField(max_length=100)
    entidad_emisora = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_certificacion


class FundoProductor(models.Model):
    nombre_fundo = models.CharField(max_length=100)
    propietario_dni_ruc = models.CharField(max_length=20)
    hectareas = models.DecimalField(max_digits=8, decimal_places=2)
    valido_exportacion = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre_fundo


class LoteRecepcionado(models.Model):
    # Relación 1:N (ForeignKey)
    fundo = models.ForeignKey(
        FundoProductor,
        on_delete=models.CASCADE,
        related_name='lotes'
    )
    codigo_lote = models.CharField(max_length=50, unique=True)
    toneladas_brutas = models.DecimalField(max_digits=8, decimal_places=2)
    porcentaje_descarte = models.DecimalField(max_digits=5, decimal_places=2)
    estado_evaluacion = models.CharField(max_length=50)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)

    # Relación N:M mediante tabla intermedia 'through'
    certificaciones = models.ManyToManyField(
        CertificacionAgricola,
        through='CertificacionLote',
        related_name='lotes'
    )

    def __str__(self):
        return f"{self.codigo_lote} - {self.fundo.nombre_fundo}"


# Relación 1:1
class EvaluacionCalidadLote(models.Model):
    lote = models.OneToOneField(
        LoteRecepcionado,
        on_delete=models.CASCADE,
        related_name='evaluacion_calidad'
    )
    nivel_brix = models.DecimalField(max_digits=4, decimal_places=2)
    firmeza_fruto = models.DecimalField(max_digits=4, decimal_places=2)
    observaciones = models.TextField(blank=True, null=True)
    fecha_evaluacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Evaluación {self.lote.codigo_lote}"


# Tabla intermedia para la relación N:M
class CertificacionLote(models.Model):
    lote = models.ForeignKey(LoteRecepcionado, on_delete=models.CASCADE)
    certificacion = models.ForeignKey(CertificacionAgricola, on_delete=models.CASCADE)
    fecha_auditoria = models.DateField()
    codigo_inspeccion = models.CharField(max_length=50)

    class Meta:
        unique_together = ('lote', 'certificacion')

    def __str__(self):
        return f"{self.lote.codigo_lote} - {self.certificacion.nombre_certificacion}"