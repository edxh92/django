from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone

from .forms import PostearForm

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

def nueva_publicacion(request):
    if request.method == "POST":
            f = PostearForm(request.POST)
            if f.is_valid():
                p = f.save(commit=False)
                # Usuario que esta logueado
                p.autor = request.user
                p.fecha_publica = timezone.now()
                p.save()
                return redirect('postear', pk=p.pk)
    else:
        f = PostearForm()
        return render(request, 'blog/nueva_publicacion.html', {'f': f})
