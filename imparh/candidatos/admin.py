from django.contrib import admin
from .models import Candidato


class CandidatoModelAdmin(admin.ModelAdmin):
    list_display = ('primeiro_nome', 'sobrenome', 'email', 'cpf')
    search_fields = ['primeiro_nome', 'sobrenome', 'email', 'cpf']
    list_filter = ('primeiro_nome', 'sobrenome', 'email', 'cpf')


admin.site.register(Candidato, CandidatoModelAdmin)
