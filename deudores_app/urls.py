from django.urls import path
from . import views # from this same directory import views

# URLConfig
urlpatterns = [
    path('', views.lista_deudores, name='lista_deudores'),
    path('<int:deudor_id>/', views.detalle_deudor, name='detalle_deudor'),
]