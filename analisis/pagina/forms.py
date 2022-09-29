from django.forms import ModelForm
from .models import *

class biseccionForm(ModelForm):
    class Meta:
        model=biseccion
        fields='__all__'