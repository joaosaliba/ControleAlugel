from django.contrib import admin

# Register your models here.
from .models import Boleta, Imovel,Pessoa,Aluguel

admin.site.register(Imovel)
admin.site.register(Pessoa)
admin.site.register(Aluguel)
admin.site.register(Boleta)
