from django import template
register = template.Library()

@register.filter
def mascara_cnpj(cnpj):
    return f'{cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'


@register.filter
def mascara_telefone(telefone):
    return f'({telefone[0:2]}) {telefone[2:11]}'