
class Atividade:
    def __init__(self, **kwargs):
        atividades = kwargs.get('atividade')
        for atividade in atividades:
            self.descricao = atividade['text']
            self.codigo = atividade['code']

    def __str__(self):
        return f"""
Descrição: {self.descricao}
Código: {self.codigo}
"""


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


# pprint(dir(response))
empresa = json.loads(response.text)
e = Empresa(
    atividade_principal=empresa['atividade_principal'],
    atividades_secundarias=empresa['atividades_secundarias'],
    nome=empresa['nome'],
    uf=empresa['uf'],
    telefone=empresa['telefone'],
    email=empresa['email'],
    data_de_abertura=empresa['abertura']
)

print(e.nome, e.uf, e.telefone, e.email, e.data_de_abertura)
