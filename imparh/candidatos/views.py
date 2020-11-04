from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from imparh.candidatos.forms import CandidatoForm
from django.shortcuts import resolve_url as r

from imparh.candidatos.models import Candidato


def new(request):
    if request.method == 'POST':
        return create(request)

    return empty_form(request)


def create(request):
    form = CandidatoForm(request.POST)

    if not form.is_valid():
        return render(request, 'candidatos/candidatos_form.html', {'form': form})

    candidato = Candidato.objects.create(**form.cleaned_data)

    return HttpResponseRedirect(r('candidatos:detail', candidato.pk))


def empty_form(request):
    return render(request, 'candidatos/candidatos_form.html',
                  {'form': CandidatoForm()})


def detail(request, pk):
    try:
        candidato = Candidato.objects.get(pk=pk)
    except Candidato.DoesNotExist:
        raise Http404

    return render(request, 'candidatos/candidato_detail.html', {'candidato': candidato})

