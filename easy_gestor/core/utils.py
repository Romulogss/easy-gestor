import re


class Utils:
    @staticmethod
    def remove_mask(cnpj):
        numeros = ''
        numeros = ''.join(re.findall(r'\d', str(cnpj)))
        return numeros