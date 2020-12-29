from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new',views.createImovelView, name='create_imovel'),
    path('storeImovel',views.storeImovel, name= 'storeImovel'),
    path('listImoveis',views.list_imovel, name='listImoveis'),
    path('editImovel/<int:pk>',views.editImovel, name='editImovel'),
]