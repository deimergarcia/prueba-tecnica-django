from django.urls import path
from . import views

urlpatterns = [
    # Clientes
    path('', views.lista_clientes, name='lista_clientes'),
    path('cliente/nuevo/', views.crear_cliente, name='crear_cliente'),
    path('cliente/<int:pk>/editar/', views.editar_cliente, name='editar_cliente'),
    path('cliente/<int:pk>/eliminar/', views.eliminar_cliente, name='eliminar_cliente'),

    # Oportunidades
    path('oportunidad/nueva/', views.crear_oportunidad, name='crear_oportunidad'),
    path('oportunidad/<int:pk>/editar/', views.editar_oportunidad, name='editar_oportunidad'),
    path('oportunidad/<int:pk>/eliminar/', views.eliminar_oportunidad, name='eliminar_oportunidad'),
    path('ver-oportunidades/', views.ver_oportunidades, name='ver_oportunidades'),
]