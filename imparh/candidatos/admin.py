from django.contrib import admin
from .models import Candidato


class CandidatoAdmin(admin.ModelAdmin):
    list_filter = ('nome_completo', 'data_nascimento', 'email', 'cpf', )
    search_fields = ['nome_completo', 'data_nascimento', 'email', 'cpf']
    list_display = ('nome_completo', 'data_nascimento', 'email', 'cpf',)


admin.site.register(Candidato, CandidatoAdmin)
