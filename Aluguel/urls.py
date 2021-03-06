from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_imovel',views.createImovelView, name='create_imovel'),
    path('storeImovel',views.storeImovel, name= 'storeImovel'),
    path('listImoveis',views.list_imovel, name='listImoveis'),
    path('editImovel/<int:pk>',views.editImovel, name='editImovel'),
    path('deleteImovel/<int:pk>',views.delete_imovel, name='deleteImovel'),

    path('create_pessoa',views.create_pessoa, name='create_pessoa'),
    path('list_pessoas',views.list_pessoa, name='list_pessoas'),
    path('edit_pessoa/<int:pk>',views.edit_pessoa, name='edit_pessoa'),
    path('delete_pessoa/<int:pk>',views.delete_pessoa, name='delete_pessoa'),

    path('alugar/',views.create_alugar, name='alugar'),
    path('edit_alugar/<int:pk>',views.edit_alugar,name='edit_alugar'),
    path('list_alugueis',views.list_alugueis,name='list_alugueis'),
    path('delete_aluguel/<int:pk>',views.delet_alugel,name='delete_aluguel'),

    path('boleta/',views.gerar_boleta,name='boleta'),
    path('lista_boletas/',views.list_boletas,name='list_boletas'),




]