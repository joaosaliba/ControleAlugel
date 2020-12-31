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







]