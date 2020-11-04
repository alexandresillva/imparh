from django.test import TestCase
from imparh.candidatos.forms import CandidatoForm


class SubscriptionFormTest(TestCase):
    def test_form_has_fields(self):
        """Form must have a fields"""
        form = CandidatoForm()
        expected = ['primeiro_nome', 'sobrenome', 'data_nascimento', 'cpf',
                    'rg_numero', 'rg_data_expedicao', 'rg_orgao_emissor', 'email']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_is_digit(self):
        """CPF must only accept digits"""
        form = self.make_validated_form(cpf='WERT1234567')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        """CPF must have 11 digits"""
        form = self.make_validated_form(cpf='1234')
        self.assertFormErrorMessage(form, 'cpf', 'CPF deve ter 11 números')

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]
        self.assertListEqual([msg], errors_list)

    def make_validated_form(self, **kwargs):
        valid = dict(
            primeiro_nome='Alexandre',
            sobrenome='Ribeiro',
            data_nascimento='16/06/1980',
            cpf='61748188372',
            rg_numero='9500220344',
            rg_data_expedicao='16/06/2002',
            rg_orgao_emissor='SSP CE',
            email='alexandresillva@gmail.com',
        )
        data = dict(valid, **kwargs)
        form = CandidatoForm(data)
        form.is_valid()
        return form