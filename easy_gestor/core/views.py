from django.shortcuts import redirect, render
from .models import (
    Empresa,
    Servico,
    ServicoPrestado,
    UnidadesFederativas
)
from .forms import EmpresaForm
# Create your views here.
from .utils import Utils


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
    try:
        mutavel = request.POST._mutable

        request.POST._mutable = not mutavel
        cnpj_com_mascara = request.POST['cnpj']
        cnpj_sem_mascara = Utils.remove_mask(cnpj_com_mascara)
        request.POST['cnpj'] = cnpj_sem_mascara

        telefone_com_mascara = request.POST['telefone']
        telefone_sem_mascara = Utils.remove_mask(telefone_com_mascara)
        request.POST['telefone'] = telefone_sem_mascara

        request.POST._mutable = mutavel
    except Exception:
        pass
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

def empresa_update(request, id):
    try:
        mutavel = request.POST._mutable

        request.POST._mutable = not mutavel
        cnpj_com_mascara = request.POST['cnpj']
        cnpj_sem_mascara = Utils.remove_mask(cnpj_com_mascara)
        request.POST['cnpj'] = cnpj_sem_mascara

        telefone_com_mascara = request.POST['telefone']
        telefone_sem_mascara = Utils.remove_mask(telefone_com_mascara)
        request.POST['telefone'] = telefone_sem_mascara

        request.POST._mutable = mutavel
    except Exception:
        pass
    empresa = Empresa.objects.get(pk=id)
    contexto = {}
    empresa_form = EmpresaForm(request.POST or None, instance=empresa)
    unidades_federativas = UnidadesFederativas
    contexto['empresa_form'] = empresa_form
    contexto['unidades_federativas'] = unidades_federativas
    contexto['empresa'] = empresa
    if empresa_form.is_valid():
        empresa_form.save()
        return redirect('empresa_index')
    return render(
        request,
        'core/empresa/form.html',
        contexto
    )