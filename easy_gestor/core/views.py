from django.shortcuts import redirect, render
from .models import (
    Empresa,
    Servico,
    ServicoPrestado,
    UnidadesFederativas
)
from .forms import EmpresaForm, ServicoForm
from .utils import Utils
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


def servico_index(request, empresa_id):
    contexto = {}
    empresa = Empresa.objects.get(pk=empresa_id)
    servicos = empresa.servicos.all()
    contexto['empresa'] = empresa
    contexto['servicos'] = servicos

    if request.method == 'POST':
        servico_form = ServicoForm(request.POST)
        if servico_form.is_valid():
            servico_form.save()
            redirect('servico_index', empresa_id)

    return render(
        request,
        'core/servico/index.html',
        contexto
    )
