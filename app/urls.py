from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pets/', views.lista_pets, name='lista_pets'),
    path('pets/<int:id>/', views.detalhe_pet, name='detalhe_pet'),
    path('pets/novo/', views.criar_pet, name='criar_pet'),
    path('pets/editar/<int:id>/', views.editar_pet, name='editar_pet'),
    path('pets/excluir/<int:id>/', views.excluir_pet, name='excluir_pet'),
]