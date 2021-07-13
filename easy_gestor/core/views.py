from django.shortcuts import redirect, render
from .models import (
    Empresa,
    Servico,
    ServicoPrestado,
    UnidadesFederativas
)
from .forms import EmpresaForm
# Create your views here.
def empresa_index(request):
    contexto = {}
    empresa_list = Empresa.objects.all()
    contexto['empresa_list'] = empresa_list

    return render(
        request,
        'core/empresa/index.html',
        contexto
    )


def empresa_create(request):
    contexto = {}
    empresa_form = EmpresaForm(request.POST or None)
    unidades_federativas = UnidadesFederativas
    contexto['empresa_form'] = empresa_form
    contexto['unidades_federativas'] = unidades_federativas
    if empresa_form.is_valid():
        empresa_form.save()
        return redirect('empresa_index')
    return render(
        request,
        'core/empresa/form.html',
        contexto
    )