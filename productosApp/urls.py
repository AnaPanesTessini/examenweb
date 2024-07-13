from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('ropadehombre/', views.ropadehombre, name='ropadehombre'),
    path('ropademujer/', views.ropademujer, name='ropademujer'),
    path('joyeria/', views.joyeria, name='joyeria'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios_crear/', views.crear_usuario, name='crear_usuario'),
    path('usuarios_actualizar/<int:pk>/', views.actualizar_usuario, name='actualizar_usuario'),
    path('usuarios_eliminar/<int:pk>/', views.eliminar_usuario, name='eliminar_usuario'),

]


    
   
