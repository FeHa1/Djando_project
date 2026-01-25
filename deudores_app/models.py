from django.db import models

class Deudor(models.Model):
    nombre_completo = models.CharField(max_length=255)
    dni = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True, null=True) # puede quedar en blanco por si no tengo los datos
    telefono = models.CharField(max_length=20, blank=True, null=True) # mismo que email, puede quedar en blanco si no tengo datos
    deuda = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_mora = models.DateField(auto_now_add=True)
    estado = models.CharField(
        max_length=50, 
            choices=[
            ('pendiente', 'Pendiente'),
            ('en_proceso', 'En Proceso'),
            ('saldada', 'Saldada')
        ], default='pendiente')
    

    def __str__(self):
        return f"{self.nombre_completo} - {self.dni} - ${self.deuda} - {self.fecha_mora}"