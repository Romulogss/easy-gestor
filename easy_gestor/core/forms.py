from django.forms import ModelForm, fields
from .models import (
    Empresa, Servico
)


class EmpresaForm(ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'


class ServicoForm(ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'