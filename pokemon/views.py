

# Create your views here.
# pokemon/views.py
from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello from Django!")