from django.shortcuts import redirect, render
from wonderwords import RandomWord

from charactergen.models import Character, Genre


def index(request):
    mystery_genre = Genre()
    mystery_genre.name = '?'
    mystery_genre.description = '?'

    mystery_character = Character()
    mystery_character.type = '?'
    mystery_character.description = '?'
    mystery_character.genre = mystery_genre

    context = {'random_character': mystery_character}
    return render(request, 'charactergen/index.html', context)


def get_random_character(request):
    random_character = Character.objects.random()
    character_type = random_character.type

    return redirect('character', character_type=character_type)


def character(request, character_type):
    character_for_rendering = Character.objects.get(type=character_type)
    random_word = RandomWord()
    random_adjective = random_word.word(include_parts_of_speech=["adjectives", ]).capitalize()
    context = {'random_character': character_for_rendering, 'random_adjective': random_adjective}
    return render(request, 'charactergen/character.html', context)
