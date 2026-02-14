from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse 

from .models import Deudor

def lista_deudores(request):
    deudores = Deudor.objects.all()  # Trae todos los deudores de la DB
    return render(request, 'deudores_app/lista_deudores.html', {'deudores': deudores})

def  detalle_deudor(request, deudor_id):
    deudor = get_object_or_404(Deudor, id=deudor_id)
    return render(request, 'deudores_app/detalle_deudor.html', {'deudor': deudor})