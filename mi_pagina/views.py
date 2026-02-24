from django.shortcuts import render
from .models import Componente

def home(request):
    # El ORM hace el "SELECT * FROM Componente" por ti
    lista_componentes = Componente.objects.all() 
    
    # Enviamos los datos al archivo HTML (que crearemos en el siguiente paso)
    return render(request, 'home.html', {'componentes': lista_componentes})