from django.forms import ModelForm, fields
from .models import (
    Empresa
)
class EmpresaForm(ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'

