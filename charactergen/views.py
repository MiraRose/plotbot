from django.http import HttpResponse

from charactergen.models import Character


def index(request):

    character = Character.objects.random()
    return HttpResponse(character.type)
