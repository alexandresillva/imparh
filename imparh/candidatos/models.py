import uuid

from django.db import models
from imparh.core import models as core


class Candidato(models.Model):
    TIPOS_DEFICIENCIAS = (
        ('1', 'Auditiva'),
        ('2', 'Visual'),
        ('3', 'Intelectual'),
        ('4', 'Física'),
        ('5', 'Outra'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome_completo = models.CharField(max_length=500)
    data_nascimento = models.DateField()
    email = models.EmailField(max_length=254)
    telefone = models.CharField(max_length=100)
    telefone_celular = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    senha = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11)
    rg_numero = models.CharField(max_length=20)
    rg_data_emissao = models.DateField()
    rg_orgao_expedicao = models.CharField(max_length=200)
    rg_uf_orgao_expedicao = models.CharField(max_length=2)
    cnh = models.CharField(max_length=50)
    cnh_emissao = models.DateField()
    cnh_data_validade = models.DateField()
    cnh_categoria = models.CharField(max_length=5)

    # ENDERECO
    endereco_cep = models.CharField(max_length=10)
    endereco_logradouro = models.CharField(max_length=500)
    endereco_numero = models.CharField(max_length=5)
    endereco_complemento = models.CharField(max_length=200)
    endereco_bairro = models.CharField(max_length=200)
    # Relacionar
    id_cidade_endereco = models.IntegerField()
    id_uf_endereco = models.IntegerField()

    nome_mae = models.CharField(max_length=500)
    data_nascimento_mae = models.DateField()

    nome_pai = models.CharField(max_length=500)
    data_nascimento_pai = models.DateField()

    sistac_nis = models.CharField(max_length=50)
    quantidade_filhos = models.IntegerField()
    deficiencia = models.CharField(
        max_length=1,
        choices=TIPOS_DEFICIENCIAS)

    # Relacionamentos
    estado_civil = core.models.ForeignKey(
        'core.EstadoCivil',
        on_delete=models.PROTECT,
        related_name='Candidato_EstadoCivil')

    escolaridade = core.models.ForeignKey(
        'core.Escolaridade',
        on_delete=models.PROTECT,
        related_name='Candidato_Escolaridade')

    sexo = core.models.ForeignKey(
        'core.Sexo',
        on_delete=models.PROTECT,
        related_name='Candidato_Sexo')

    tipo_documento_identificacao = core.models.ForeignKey(
        'core.TipoDocumentoIdentificacao',
        on_delete=models.PROTECT,
        related_name='Candidato_TipoDocumentoIdentificacao')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'candidato'
        verbose_name = "Candidato"
        verbose_name_plural = "Candidatos"

    def __str__(self):
        return self.nome_completo
