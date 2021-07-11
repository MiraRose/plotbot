from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from charactergen.models import Character


def index(request):
    template = loader.get_template('charactergen/index.html')
    context = {'random_character': 'blah', }
    return HttpResponse(template.render(context, request))


def get_random_character(request):
    character = Character.objects.random()
    return HttpResponseRedirect(reverse('index'), {'random_character': character})
