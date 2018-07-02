from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Character

# Create your views here.


def index(request):
    character_latest = Character.objects.order_by('-chr_name')
    template = loader.get_template('creator/index.html')
    context = {
        'character_latest': character_latest
    }
    return HttpResponse(template.render(context, request))


def detail(request, char_name):
    try:
        character = Character.objects.filter(chr_name = char_name)

    except Character.DoesNotExist:
        raise Http404("Character does not exist")
    return render(request, 'creator/detail.html', {'character': character})
