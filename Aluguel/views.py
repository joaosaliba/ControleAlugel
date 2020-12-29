from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ImovelForm
from .models import Imovel
from django.contrib import messages

# Create your views here.
def index(request):
     return render(request, 'base.html')

# def create_imovel(request):
#      form = ImovelForm(request.POST or None)
#      if form.is_valid():
#           form.save()
#           return redirect('listImoveis')
#      return render(request, 'formImovel.html', {'form':form})

def createImovelView(request):
     return render(request,'createimovel.html')

def storeImovel(request):
     imovel = Imovel()
     imovel.cep= request.POST.get('cep')
     imovel.endereco= request.POST.get('endereco')
     imovel.save()
     messages.success(request,'Imovel adiconado com sucesso')
     return redirect('/listImoveis')


def editImovel(request,pk):
     imovel= Imovel.objects.get(id=pk)

     if request.method =="GET":
          return render(request,'editImovel.html',{'imovel':imovel})
     else:
          imovel.id = pk
          imovel.cep= request.POST.get('cep')
          imovel.endereco= request.POST.get('endereco')
          imovel.save()
          messages.success(request,'Imovel adiconado com sucesso')
          return redirect('/listImoveis')

     

     

def list_imovel(request):
     imoveis = Imovel.objects.all()
     return render(request, 'listImovel.html',{'imoveis':imoveis})