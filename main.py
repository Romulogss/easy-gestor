from module import (
    get_empresa_by_cnpj,
    shape_empresa,
    get_cnpj,
    cnpj_is_valid
)

while True:
    print("Bem-vindo ao consultor de CNPJ")
    cnpj = get_cnpj()
    while not cnpj_is_valid(cnpj):
        print("CNPJ não é válido")
        cnpj = get_cnpj()
    empresa_json = get_empresa_by_cnpj(cnpj)
    empresa = shape_empresa(empresa_json)
    print("Nome: " + empresa.nome)
    print("CNPJ: " + f"{cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}")
    print("Aberta em: " + empresa.data_de_abertura)
    print("Telefone para contato: " + empresa.telefone)
    print("E-mail para contato: " + empresa.email)
    print("Atividade principal" + str(empresa.atividade_principal))
    print("Atividades secundárias")
    for atividade in empresa.atividades_secundarias:
        print(atividade)

    outra_busca = input("Você deseja buscar outro CNPJ [s/n]: ")
    if outra_busca.lower() == 'n':
        break

print("Obrigado por utilizar meu programinha <3")
