from django.forms import ModelForm
from .models import (
    Empresa,
    Servico,
    ServicoPrestado
)


class EmpresaForm(ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'


class ServicoForm(ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'


class PrestacaoServicoForm(ModelForm):
    class Meta:
        model = ServicoPrestado
        fields = '__all__'