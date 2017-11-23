from django.conf.urls import url, include

from apps.eventos.views import index, evento_view, eventos_list, eventos_edit, eventos_delete, \
							   EventoList, EventoCreate, EventoUpdate, EventoDelete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^novo$', EventoCreate.as_view(), name='evento_novo'),
    url(r'^listar$', EventoList.as_view(), name='evento_listar'),
    url(r'^editar/(?P<pk>\d+)$', EventoUpdate.as_view(), name='evento_editar'),
    url(r'^eliminar/(?P<pk>\d+)$', EventoDelete.as_view(), name='evento_eliminar'),
]