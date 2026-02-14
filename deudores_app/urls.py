from django.urls import path
from . import views # from this same directory import views

# URLConfig
urlpatterns = [
    path('', views.lista_deudores, name='lista_deudores'),
    path('<int:deudor_id>/', views.detalle_deudor, name='detalle_deudor'),
    path('nuevo/', views.crear_deudor, name='crear_deudor'), 
    path('<int:deudor_id>/editar/', views.editar_deudor, name='editar_deudor'), 
    path('<int:deudor_id>/eliminar/', views.eliminar_deudor, name='eliminar_deudor'),
]