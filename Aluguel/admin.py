from django.contrib import admin

# Register your models here.
from .models import Imovel,Pessoa,Aluguel

admin.site.register(Imovel)
admin.site.register(Pessoa)
admin.site.register(Aluguel)