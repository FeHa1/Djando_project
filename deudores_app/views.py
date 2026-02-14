from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse 

from .models import Deudor
from .forms import DeudorForm

def lista_deudores(request):
    deudores = Deudor.objects.all()  # Brings all debtors from DB
    return render(request, 'deudores_app/lista_deudores.html', {'deudores': deudores})

def  detalle_deudor(request, deudor_id):
    deudor = get_object_or_404(Deudor, id=deudor_id)
    return render(request, 'deudores_app/detalle_deudor.html', {'deudor': deudor})

def crear_deudor(request):
    if request.method == 'POST':
        form = DeudorForm(request.POST)
        if form.is_valid(): # If the form is valid, we save it in the database.
            form.save()
            return redirect('lista_deudores')
    else:
        form = DeudorForm()
    
    return render(request, 'deudores_app/crear_deudor.html', {'form': form})

def editar_deudor(request, deudor_id):

    deudor = get_object_or_404(Deudor, id=deudor_id)
    
    if request.method == 'POST':
        form = DeudorForm(request.POST, instance=deudor)
        if form.is_valid():
            form.save()
            return redirect('detalle_deudor', deudor_id=deudor.id)
    else:
        form = DeudorForm(instance=deudor)
    
    return render(request, 'deudores_app/editar_deudor.html', {'form': form, 'deudor': deudor})

def eliminar_deudor(request, deudor_id):
    deudor = get_object_or_404(Deudor, id=deudor_id)
    
    if request.method == 'POST':
        deudor.delete()
        return redirect('lista_deudores')
    
    return render(request, 'deudores_app/eliminar_deudor.html', {'deudor': deudor})