# Generated by Django 3.1.2 on 2020-10-21 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('candidatos', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='escolaridade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Candidato_Escolaridade', to='core.escolaridade'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='estado_civil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Candidato_EstadoCivil', to='core.estadocivil'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='sexo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Candidato_Sexo', to='core.sexo'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='tipo_documento_identificacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Candidato_TipoDocumentoIdentificacao', to='core.tipodocumentoidentificacao'),
        ),
    ]
