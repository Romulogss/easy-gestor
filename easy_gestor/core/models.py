from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now

# Create your models here.


class UnidadesFederativas(models.TextChoices):
    AC = 'AC', _('Acre')
    AL = 'AL', _('Alagoas')
    AP = 'AP', _('Amapá')
    AM = 'AM', _('Amazonas')
    BA = 'BA', _('Bahia')
    CE = 'CE', _('Ceará')
    ES = 'ES', _('Espírito Santo')
    GO = 'GO', _('Goiás')
    MA = 'MA', _('Maranhão')
    MT = 'MT', _('Mato Grosso')
    MS = 'MS', _('Mato Grosso do Sul')
    MG = 'MG', _('Minas Gerais')
    PA = 'PA', _('Pará')
    PB = 'PB', _('Paraíba')
    PE = 'PE', _('Pernambuco')
    PI = 'PI', _('Piauí')
    RJ = 'RJ', _('Rio de Janeiro')
    RS = 'RS', _('Rio Grande do Sul')
    RO = 'RO', _('Rondânia')
    RR = 'RR', _('Roraima')
    SC = 'SC', _('Santa Catarina')
    SP = 'SP', _('São Paulo')
    SE = 'SE', _('Sergipe')
    TO = 'TO', _('Tocantins')
    DF = 'DF', _('Distrito Federal')


class Empresa(models.Model):

    nome = models.CharField(
        max_length=150,
        null=False,
        blank=False
    )
    cnpj = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )
    telefone = models.CharField(
        max_length=11,
        null=False,
        blank=False
    )
    email = models.EmailField(
        null=False,
        blank=False
    )
    uf = models.CharField(
        max_length=2,
        choices=UnidadesFederativas.choices,
        default=UnidadesFederativas.PA,
        null=False,
        blank=False
    )

    def __str__(self):
        return f'{self.nome} | {self.cnpj}'


class Servico(models.Model):

    nome = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    descricao = models.TextField(
        null=False,
        blank=False
    )
    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False
    )
    empresa = models.ForeignKey(
        Empresa,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f'{self.nome} | {self.descricao[0:25]}...'


class ServicoPrestado(models.Model):

    data = models.DateField(
        default=now().date(),
        null=False,
        blank=False
    )
    empresa_prestadora = models.ForeignKey(
        Empresa,
        related_name='servico_prestado',
        on_delete=models.DO_NOTHING,
        null=False,
        blank=False
    )
    empresa_cliente = models.ForeignKey(
        Empresa,
        related_name='servico_recebido',
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    servico = models.ForeignKey(
        Servico,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    def __str__(self) -> str:
        return f'{self.data} | {self.empresa.nome} | {self.servico.nome}'
