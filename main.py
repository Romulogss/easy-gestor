import requests as request
from pprint import pprint
import json


def cnpj_is_valid(cnpj):
    valido = True
    if len(cnpj) < 14:
        valido = False
    else:
        response = request.get('https://www.receitaws.com.br/v1/cnpj/065284598000112')
        if response.text['status'] == 'ERROR':
            valido = False
    return valido


response = request.get('https://www.receitaws.com.br/v1/cnpj/065284598000112')


def get_cnpj():
    return input("Informe o CNPJ que deseja buscar (somente números): ")


while True:
    print("Bem-vindo ao consultor de CNPJ")
    cnpj = get_cnpj()
    while not cnpj_is_valid(cnpj):
        print("CNPJ não é válido")
        cnpj = get_cnpj()

