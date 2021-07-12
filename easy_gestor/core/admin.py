from .models import (
    Empresa,
    Servico,
    ServicoPrestado
)
from django.contrib import admin

# Register your models here.
admin.site.register(Empresa)
admin.site.register(Servico)
admin.site.register(ServicoPrestado)
