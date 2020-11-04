from django import forms
from django.core.exceptions import ValidationError


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('CPF deve ter somente números', 'digits')

    if len(value) != 11:
        raise ValidationError('CPF deve ter 11 números', 'length')


class CandidatoForm(forms.Form):
    primeiro_nome = forms.CharField(label='Primeiro nome', required='O campo primeiro nome é obrigatório')
    sobrenome = forms.CharField(label='Sobrenome')
    data_nascimento = forms.DateField(label='Data de nascimento')
    cpf = forms.CharField(label='CPF', validators=[validate_cpf])
    rg_numero = forms.CharField(label='RG')
    rg_data_expedicao = forms.DateTimeField(label='Data de expedição RG')
    rg_orgao_emissor = forms.CharField(label='Órgão emissor RG')
    email = forms.EmailField(label='Email')

