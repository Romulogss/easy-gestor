from django.db import models

class EmpresaManager(models.Manager):
    def filter_by_param(self, param, value):
        empresas = super().filter(param=value)
        return empresas