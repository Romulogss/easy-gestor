"""easy_gestor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from core.views import (
    empresa_index,
    empresa_create,
    empresa_update,
    empresa_delete,
    servico_index,
    servico_update,
    servico_delete,
)
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', empresa_index, name='empresa_index'),
    path('empresa/create', empresa_create, name='empresa_create'),
    path('empresa/update/<str:id>', empresa_update, name='empresa_update'),
    path('empresa/delete/<str:id>', empresa_delete, name='empresa_delete'),

    path('servicos/<str:empresa_id>', servico_index, name='servicos_index'),
    path('servicos/update/<str:id>', servico_update, name='servico_update'),
    path('servicos/delete/<str:id>', servico_delete, name='servico_delete'),

    path('admin/', admin.site.urls),
]
