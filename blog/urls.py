from django.conf.urls import include, url
from . import views


urlpatterns = [
        url(r'^$', views.listar_publicacion),
        #enviar lel direccionamiento con la pagina y los envia el id del post que se va a
        # emplear para desplejar el resultado de la busqueda
        url(r'^postear/(?P<pk>[0-9]+)/$', views.detalle_pub, name='postear'),
        url(r'^postear/nuevo/$',views.nueva_publicacion,name='nueva_publicacion'),
    ]
