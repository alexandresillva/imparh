import uuid

from django.db import models


class Candidato(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    primeiro_nome = models.CharField('Primeiro nome', max_length=100)
    sobrenome = models.CharField(max_length=150)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11)
    rg_numero = models.CharField(max_length=20)
    rg_data_expedicao = models.DateField()
    rg_orgao_emissor = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'candidato'
        verbose_name = "Candidato"
        verbose_name_plural = "Candidatos"

    def __str__(self):
        return self.primeiro_nome
