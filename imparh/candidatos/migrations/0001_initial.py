# Generated by Django 3.1.2 on 2020-10-21 20:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome_completo', models.CharField(max_length=500)),
                ('data_nascimento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=100)),
                ('telefone_celular', models.CharField(max_length=100)),
                ('login', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=20)),
                ('cpf', models.CharField(max_length=11)),
                ('rg_numero', models.CharField(max_length=20)),
                ('rg_data_emissao', models.DateField()),
                ('rg_orgao_expedicao', models.CharField(max_length=200)),
                ('rg_uf_orgao_expedicao', models.CharField(max_length=2)),
                ('cnh', models.CharField(max_length=50)),
                ('cnh_emissao', models.DateField()),
                ('cnh_data_validade', models.DateField()),
                ('cnh_categoria', models.CharField(max_length=5)),
                ('endereco_cep', models.CharField(max_length=10)),
                ('endereco_logradouro', models.CharField(max_length=500)),
                ('endereco_numero', models.CharField(max_length=5)),
                ('endereco_complemento', models.CharField(max_length=200)),
                ('endereco_bairro', models.CharField(max_length=200)),
                ('id_cidade_endereco', models.IntegerField()),
                ('id_uf_endereco', models.IntegerField()),
                ('nome_mae', models.CharField(max_length=500)),
                ('data_nascimento_mae', models.DateField()),
                ('nome_pai', models.CharField(max_length=500)),
                ('data_nascimento_pai', models.DateField()),
                ('sistac_nis', models.CharField(max_length=50)),
                ('quantidade_filhos', models.IntegerField()),
                ('deficiencia', models.CharField(choices=[('1', 'Auditiva'), ('2', 'Visual'), ('3', 'Intelectual'), ('4', 'Física'), ('5', 'Outra')], max_length=1)),
            ],
            options={
                'verbose_name': 'Candidato',
                'verbose_name_plural': 'Candidatos',
                'db_table': 'candidato',
            },
        ),
    ]