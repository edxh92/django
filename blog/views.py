from django.shortcuts import render
from django.utils import timezone

from .models import Publicar

# Create your views here.
def listar_publicacion(request):
        publi = Publicar.objects.filter(fecha_publica__lte=timezone.now()).order_by('fecha_publica')
        # publi = Publicar.objects.())
        return render(request,'blog/listar_publicacion.html', {'publi':publi})
