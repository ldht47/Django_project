from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>¡Hola Mundo! Este es mi primer sitio en Django.</h1>")