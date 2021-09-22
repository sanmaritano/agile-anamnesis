from django.db import models
from django.db.models.expressions import When
from django.utils.translation import gettext_lazy as _

class Consult(models.Model):

    class GeneroChoices(models.TextChoices):
        MASCULINO = 'M', _('Masculino')
        FEMININO = 'F', _('Feminino')

    class RelacionamentoChoices(models.TextChoices):
        SOLTEIRO = 'S', _('Solteiro(a)')
        CASADO = 'C', _('Casado(a)')
        DIVORCIADO = 'D', _('Divorciado(a)')
        VIUVO = 'V', _('Viúvo(a)')

    class EstadosUF(models.TextChoices):
        AC = 'AC', _('Acre')
        AL = 'AL', _('Alagoas')
        AP = 'AP', _('Amapá')
        AM = 'AM', _('Amazonas')
        BA = 'BA', _('Bahia')
        CE = 'CE', _('Ceará')
        DF = 'DF', _('Distrito Federal')
        ES = 'ES', _('Espírito Santo')
        GO = 'GO', _('Goiás')
        MA = 'MA', _('Maranhão')
        MT = 'MT', _('Mato Grosso')
        MS = 'MS', _('Mato Grosso do Sul')
        MG = 'MG', _('Minas Gerais')
        PA = 'PA', _('Pará')
        PB = 'PB', _('Paraíba')
        PR = 'PR', _('Paraná')
        PE = 'PE', _('Pernambuco')
        PI = 'PI', _('Piauí')
        RJ = 'RJ', _('Rio de Janeiro')
        RN = 'RN', _('Rio Grande do Norte')
        RS = 'RS', _('Rio Grande do Sul')
        RO = 'RO', _('Rondônia')
        RR = 'RR', _('Roraima')
        SC = 'SC', _('Santa Catarina')
        SP = 'SP', _('São Paulo')
        SE = 'SE', _('Sergipe')
        TO = 'TO', _('Tocantins')
    
    nome = models.CharField(max_length=100, null=False)
    cpf = models.CharField(max_length=12, unique=True)
    nascimento = models.CharField(max_length=100, )

    sexo = models.CharField(max_length=100, 
        choices=GeneroChoices.choices, 
        default=GeneroChoices.FEMININO)

    estado_civil = models.CharField(max_length=100, 
        choices=RelacionamentoChoices.choices, 
        default=RelacionamentoChoices.SOLTEIRO)

    email = models.EmailField(max_length=100)
    endereco = models.CharField(max_length=100)
    

    UF = models.CharField(max_length=100, 
        choices=EstadosUF.choices, 
        default=None)

    numero_contato = models.CharField(max_length=11, null=False)
    data = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nome
