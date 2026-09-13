from django.shortcuts import render, redirect, get_object_or_404
from .models import FundoProductor, LoteRecepcionado
from .forms import FundoProductorForm, LoteRecepcionadoForm
from .models import FundoProductor, LoteRecepcionado, CertificacionLote
from .forms import FundoProductorForm, LoteRecepcionadoForm, CertificacionLoteForm

# Vistas de FundoProductor
def fundo_list(request):
    fundos = FundoProductor.objects.all()
    return render(request, 'agrotrace/fundo_list.html', {'fundos': fundos})

def fundo_create(request):
    if request.method == 'POST':
        form = FundoProductorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agrotrace:fundo_list')
    else:
        form = FundoProductorForm()
    return render(request, 'agrotrace/fundo_form.html', {'form': form, 'title': 'Nuevo Fundo'})

def fundo_update(request, pk):
    fundo = get_object_or_404(FundoProductor, pk=pk)
    if request.method == 'POST':
        form = FundoProductorForm(request.POST, instance=fundo)
        if form.is_valid():
            form.save()
            return redirect('agrotrace:fundo_list')
    else:
        form = FundoProductorForm(instance=fundo)
    return render(request, 'agrotrace/fundo_form.html', {'form': form, 'title': 'Editar Fundo'})

def fundo_delete(request, pk):
    fundo = get_object_or_404(FundoProductor, pk=pk)
    if request.method == 'POST':
        fundo.delete()
        return redirect('agrotrace:fundo_list')
    return render(request, 'agrotrace/fundo_confirm_delete.html', {'object': fundo, 'type': 'Fundo'})

# Vistas de LoteRecepcionado
def lote_list(request):
    # Optimización de consultas ORM
    # select_related para relaciones 1:1 y 1:N (JOIN en SQL)
    # prefetch_related para relaciones N:M (consulta separada + join en memoria)
    lotes = LoteRecepcionado.objects.select_related(
        'fundo',
        'evaluacion_calidad'
    ).prefetch_related(
        'certificaciones'
    )
    return render(request, 'agrotrace/lote_list.html', {'lotes': lotes})

def lote_create(request):
    if request.method == 'POST':
        form = LoteRecepcionadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agrotrace:lote_list')
    else:
        form = LoteRecepcionadoForm()
    return render(request, 'agrotrace/lote_form.html', {'form': form, 'title': 'Nuevo Lote'})

def lote_update(request, pk):
    lote = get_object_or_404(LoteRecepcionado, pk=pk)
    if request.method == 'POST':
        form = LoteRecepcionadoForm(request.POST, instance=lote)
        if form.is_valid():
            form.save()
            return redirect('agrotrace:lote_list')
    else:
        form = LoteRecepcionadoForm(instance=lote)
    return render(request, 'agrotrace/lote_form.html', {'form': form, 'title': 'Editar Lote'})

def lote_delete(request, pk):
    lote = get_object_or_404(LoteRecepcionado, pk=pk)
    if request.method == 'POST':
        lote.delete()
        return redirect('agrotrace:lote_list')
    return render(request, 'agrotrace/lote_confirm_delete.html', {'object': lote, 'type': 'Lote'})

def certificacionlote_list(request):
    asignaciones = CertificacionLote.objects.select_related('lote', 'certificacion').all()
    return render(request, 'agrotrace/certificacionlote_list.html', {'asignaciones': asignaciones})

def certificacionlote_create(request):
    if request.method == 'POST':
        form = CertificacionLoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agrotrace:certificacionlote_list')
    else:
        form = CertificacionLoteForm()
    return render(request, 'agrotrace/certificacionlote_form.html', {'form': form, 'title': 'Nueva Certificación de Lote'})

def certificacionlote_update(request, pk):
    asignacion = get_object_or_404(CertificacionLote, pk=pk)
    if request.method == 'POST':
        form = CertificacionLoteForm(request.POST, instance=asignacion)
        if form.is_valid():
            form.save()
            return redirect('agrotrace:certificacionlote_list')
    else:
        form = CertificacionLoteForm(instance=asignacion)
    return render(request, 'agrotrace/certificacionlote_form.html', {'form': form, 'title': 'Editar Certificación de Lote'})

def certificacionlote_delete(request, pk):
    asignacion = get_object_or_404(CertificacionLote, pk=pk)
    if request.method == 'POST':
        asignacion.delete()
        return redirect('agrotrace:certificacionlote_list')
    return render(request, 'agrotrace/certificacionlote_confirm_delete.html', {'object': asignacion, 'type': 'Certificación de Lote'})