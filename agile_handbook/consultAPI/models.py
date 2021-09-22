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

class Anamnese(models.Model):

    class BooleanChoices(models.TextChoices):
        TRUE = 'S', _('Sim')
        FALSE = 'N', _('Nao')

    class HigieneChoices(models.TextChoices):
        BOA = 'B', _('Boa')
        REGULAR = 'R', _('Regular')
        RUIM = 'r', _('Ruim')

    class Present(models.TextChoices):
        AUSENTE = 'A', _('Ausente')
        PRESENTE = 'P', _('Presente')

    class HalitoseChoices(models.TextChoices):
        AUSENTE = 'A', _('Ausente')
        LEVE = 'L', _('Leve')
        FORTE = 'F', _('Forte')      

    class MucosaChoices(models.TextChoices):
        NORMAL = 'N', _('Normal')
        ALTERADA = 'A', _('Alterada')

    class ApinhamentoChoices(models.TextChoices):
        AUSENTE = 'A', _('Ausente')
        LEVE = 'L', _('Leve')
        SEVERO = 'S', _('Severo')

    #Anamnese

    problema_saude = models.CharField(
        max_length=3, 
        choices=BooleanChoices.choices, 
        default=BooleanChoices.FALSE)
    
    When(problema_saude=BooleanChoices.TRUE, 
    then=models.CharField(max_length=100)) 

    
    tratamnento_medico = models.CharField(
        max_length=3, 
        choices=BooleanChoices.choices, 
        default=BooleanChoices.FALSE)
    
    When(tratamnento_medico=BooleanChoices.TRUE, 
    then=models.CharField(max_length=100)) 


    medicamento = models.CharField(
        max_length=3, 
        choices=BooleanChoices.choices, 
        default=BooleanChoices.FALSE)
    
    When(medicamento=BooleanChoices.TRUE, then=models.CharField(max_length=100)) 
    
    alergia_medicamento = models.CharField(max_length=3, 
        choices=BooleanChoices.choices, 
        default=BooleanChoices.FALSE)
    
    When(alergia_medicamento=BooleanChoices.TRUE, then=models.CharField(max_length=100)) 

    
    fumante = models.CharField(
        max_length=3, 
        choices=BooleanChoices.choices, 
        default=BooleanChoices.FALSE)

    sangramento_gengiva = models.CharField(
        max_length=3, 
        choices=BooleanChoices.choices, 
        default=BooleanChoices.FALSE)

    sensibilidade = models.CharField(
        max_length=3, 
        choices=BooleanChoices.choices, 
        default=BooleanChoices.FALSE)

    roi_unhas = models.CharField(
        max_length=3, 
        choices=BooleanChoices.choices, 
        default=BooleanChoices.FALSE)

    morder_caneta = models.CharField(
        max_length=3, 
        choices=BooleanChoices.choices, 
        default=BooleanChoices.FALSE)

    fio_dental = models.CharField(
        max_length=3, 
        choices=BooleanChoices.choices, 
        default=BooleanChoices.FALSE)
    
    When(fio_dental=BooleanChoices.TRUE, then=models.CharField(max_length=100)) 

    outro_habito = models.TextField(max_length=300)
    
    #Intra-oral

    higiene = models.CharField(max_length=1, 
        choices = HigieneChoices.choices, 
        default=HigieneChoices.BOA)

    halitose = models.CharField(max_length=1, 
    choices=Present.choices, 
    default=Present.PRESENTE)

    mucosa = models.CharField(max_length=1, 
    choices=Present.choices, 
    default=Present.PRESENTE)

    lingua = models.CharField(max_length=100)
    palato = models.CharField(max_length=100)
    palato_mole = models.CharField(max_length=100)
    assoalho_bucal = models.CharField(max_length=100)
    labios = models.CharField(max_length=100)

    #Periodontal

    placa_bacteriana_invisivel = models.CharField(max_length=1,
     choices=Present.choices, 
     default=Present.PRESENTE)

    sangramento_gengival = models.CharField(max_length=1, 
    choices=Present.choices, 
    default=Present.PRESENTE)

    tartaro = models.CharField(max_length=1, 
    choices=Present.choices, 
    default=Present.PRESENTE)

    mobilidade_dental = models.CharField(max_length=1, 
    choices=Present.choices, 
    default=Present.PRESENTE)

    #Ortodontico

    apinhamento = models.CharField(max_length=1, 
    choices=ApinhamentoChoices.choices, 
    default=ApinhamentoChoices.AUSENTE)

    diastemas = models.CharField(max_length=1, 
    choices=Present.choices, 
    default=Present.PRESENTE)

    observacoes = models.TextField(blank=True)
    tratamento = models.TextField(blank=True)
