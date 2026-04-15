# pokemon/views.py
from django.http import JsonResponse


POKEMON_DATA = {
    "pikachu": {"name": "pikachu", "type": "electric", "base_experience": 112},
    "bulbasaur": {"name": "bulbasaur", "type": "grass", "base_experience": 64},
    "charmander": {"name": "charmander", "type": "fire", "base_experience": 62},
}


def pokemon_list(request):
    data = list(POKEMON_DATA.values())
    return JsonResponse(data, safe=False)