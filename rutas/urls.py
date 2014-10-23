from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'users.views.home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #USUARIOS
    url(r'^login/$', 'users.views.iniciar_sesion'),
    url(r'^logout/$', 'users.views.cerrar_sesion'),
    url(r'^users/$', 'users.views.privado'),
    url(r'^users/new/$', 'users.views.new_user'),
    url(r'^users/edit/$', 'users.views.edit_perfil'),
    url(r'^users/reset/pass/$', 'users.views.cambiar_password'),

    #ASOCIACIONES
    url(r'^association/$', 'asociaciones.views.index_asociacion'),
    url(r'^association/new/$', 'asociaciones.views.new_association'),
    url(r'^association/list/update/$', 'asociaciones.views.list_association_update'),
    url(r'^association/(?P<association_id>\d+)/update/$', 'asociaciones.views.update_association'),
    url(r'^association/list/detail/$', 'asociaciones.views.list_detail_association'),

    url(r'^association/my/$', 'asociaciones.views.mi_association'),

    url(r'^association/mapa/ajax/$', 'asociaciones.views.mapa_association_ajax'),

    #LINEAS
    url(r'^line/my/$', 'lineas.views.mis_lineas'),
    url(r'^line/my/add/$', 'lineas.views.add_mi_linea'),

    url(r'^line/mapa/$', 'lineas.views.mapa'),

)
