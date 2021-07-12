import json

import requests


class Atividade:
    def __init__(self, **kwargs):
        atividades = kwargs.get('atividade')
        for atividade in atividades:
            self.descricao = atividade['text']
            self.codigo = atividade['code']

    def __str__(self):
        return f"""
Descrição: {self.descricao}
Código: {self.codigo}"""


class Empresa:
    def __init__(self, **kwargs):
        self.atividade_principal = Atividade(
            atividade=kwargs.get('atividade_principal')
        )
        atividades_secundarias = []
        for atividade in kwargs.get('atividades_secundarias'):
            atividades_secundarias.append(Atividade(atividade=[atividade]))
        self.atividades_secundarias = atividades_secundarias
        self.nome = kwargs.get('nome')
        self.uf = kwargs.get('uf')
        self.telefone = kwargs.get('telefone')
        self.email = kwargs.get('email')
        self.data_de_abertura = kwargs.get('data_de_abertura')


def cnpj_is_valid(cnpj):
    valido = True
    if len(cnpj) != 14:
        valido = False
    else:
        response = requests.get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj}')
        response = json.loads(response.text)
        if response['status'] == 'ERROR':
            valido = False
    return valido


def get_cnpj():
    return input("Informe o CNPJ que deseja buscar (somente números): ")


def get_empresa_by_cnpj(cnpj):
    response = requests.get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj}')
    response_json = response.json()
    return {
        'atividade_principal': response_json['atividade_principal'],
        'atividades_secundarias': response_json['atividades_secundarias'],
        'nome': response_json['nome'],
        'uf': response_json['uf'],
        'telefone': response_json['telefone'],
        'email': response_json['email'],
        'data_de_abertura': response_json['abertura']
    }


def shape_empresa(empresa_dict):
    return Empresa(
        atividade_principal=empresa_dict['atividade_principal'],
        atividades_secundarias=empresa_dict['atividades_secundarias'],
        nome=empresa_dict['nome'],
        uf=empresa_dict['uf'],
        telefone=empresa_dict['telefone'],
        email=empresa_dict['email'],
        data_de_abertura=empresa_dict['data_de_abertura']
    )
