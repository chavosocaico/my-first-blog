from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'apagar_materiais/(?P<pk>[0-9]+)/$',views.apagar_materiais, name='apagar_materiais'),
	url(r'apagar_salas/(?P<pk>[0-9]+)/$',views.apagar_salas, name='apagar_salas'),
	url(r'cancelar_reserva_sala/(?P<pk>[0-9]+)/$', views.cancelar_RSala, name = 'cancelar_reserva_sala'),
	url(r'cancelar_reserva_material/(?P<pk>[0-9]+)/$', views.cancelar_RMaterial, name = 'cancelar_reserva_material'),
	url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
	url(r'^listar_salas/$', views.listar_salas, name='listar_salas'),
	url(r'^listar_materiais/$', views.listar_materiais, name='listar_materiais'),
	url(r'^cadastrar_salas/$', views.cadastrar_salas, name='cadastrar_salas'),
	url(r'^cadastrar_materiais/$', views.cadastrar_materiais, name='cadastrar_materiais'),
	url(r'^inicio/$', views.inicio, name='inicio'),
	url(r'^reservar_salas/(?P<pk>[0-9]+)/$', views.reservar_salas, name='reservar_salas'),
	url(r'^reservar_materiais/(?P<pk>[0-9]+)/$', views.reservar_materiais, name='reservar_materiais'),
	url(r'^materiais_reservados/$', views.materiais_reservados, name='materiais_reservados'),
	url(r'^salas_reservadas/$', views.salas_reservadas, name='salas_reservadas'),
	url(r'^deferir_reserva_material/(?P<pk>[0-9]+)/$', views.deferir_reserva_material, name='deferir_reserva_material'),
	url(r'^indeferir_reserva_material/(?P<pk>[0-9]+)/$', views.indeferir_reserva_material, name='indeferir_reserva_material'),
	url(r'^deferir_reserva_sala/(?P<pk>[0-9]+)/$', views.deferir_reserva_sala, name='deferir_reserva_sala'),
	url(r'^indeferir_reserva_sala/(?P<pk>[0-9]+)/$', views.indeferir_reserva_sala, name='indeferir_reserva_sala'),
	url(r'^editar_sala/(?P<pk>[0-9]+)/$', views.editar_sala, name='editar_sala'),
	url(r'^editar_material/(?P<pk>[0-9]+)/$', views.editar_material, name='editar_material'),
]
