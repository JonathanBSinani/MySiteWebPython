from django.conf.urls import url, include

from django.contrib.auth.decorators import login_required

from apps.eventos.views import index, evento_view, eventos_list, eventos_edit, eventos_delete, \
							   EventoList, EventoCreate, EventoUpdate, EventoDelete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^novo$', login_required(EventoCreate.as_view()), name='evento_novo'),
    url(r'^listar$', login_required(EventoList.as_view()), name='evento_listar'),
    url(r'^editar/(?P<pk>\d+)$', login_required(EventoUpdate.as_view()), name='evento_editar'),
    url(r'^eliminar/(?P<pk>\d+)$', login_required(EventoDelete.as_view()), name='evento_eliminar'),
]