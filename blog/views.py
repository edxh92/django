from django.shortcuts import render,get_object_or_404
from django.utils import timezone

from .models import Publicar

# Create your views here.
def listar_publicacion(request):
        publi = Publicar.objects.filter(fecha_publica__lte=timezone.now()).order_by('fecha_publica')
        # publi = Publicar.objects.())
        return render(request,'blog/listar_publicacion.html', {'publi':publi})
        
def detalle_pub(request,pk):
        # si no encuentra el valor devuelve la pagina 404 que dice que no esta la pagina
        p=get_object_or_404(Publicar,pk=pk)
        # publi = Publicar.objects.())
        return render(request,'blog/detalle_pub.html', {'p':p})
