from django.db import models

# Create your models here.

class biseccion(models.Model):
    Xi=models.FloatField()
    Xs=models.FloatField()
    Tol=models.FloatField()
    Niter=models.FloatField()
    funcion=models.CharField(max_length=50)


