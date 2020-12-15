from django.shortcuts import render
from django.http import HttpResponse
import .models import Alugel, Pessoa, Imovel

# Create your views here.
def index(request):
    return HttpResponse('Hello, world.')