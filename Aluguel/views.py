from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ImovelForm
from .models import Imovel, Pessoa,Aluguel
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
     return render(request,'imovel/createimovel.html')

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
          return render(request,'imovel/editImovel.html',{'imovel':imovel})
     else:
          imovel.id = pk
          imovel.cep= request.POST.get('cep')
          imovel.endereco= request.POST.get('endereco')
          imovel.save()
          messages.success(request,'Imovel adiconado com sucesso')
          return redirect('/listImoveis')

     
def list_imovel(request):
     imoveis = Imovel.objects.all()
     return render(request, 'imovel/listImovel.html',{'imoveis':imoveis})

def delete_imovel(request,pk):
     imovel = Imovel.objects.get(id=pk)
     imovel.delete()
     messages.success(request, "Imovel Deletado com Sucesso")
     return redirect('/listImoveis')

def create_pessoa(request):
     pessoa = Pessoa()
     if request.method =="GET":
          return render(request,'pessoa/createPessoa.html',{'pessoa':pessoa})
     else:
          pessoa.nome= request.POST.get('nome')
          pessoa.cpf= request.POST.get('cpf')
          pessoa.rg= request.POST.get('rg')
          pessoa.telefone= request.POST.get('telefone')
          pessoa.save()
          messages.success(request,'Pessoa adiconado com sucesso')
          return redirect('/list_pessoas')

def list_pessoa(request):
     pessoas = Pessoa.objects.all()
     return render(request, 'pessoa/listPessoas.html',{'pessoas':pessoas})

def edit_pessoa(request,pk):
     pessoa = Pessoa.objects.get(id=pk)

     if request.method =="GET":
          return render(request,'pessoa/editPessoa.html',{'pessoa':pessoa})
     else:
          pessoa.id =pk
          pessoa.nome= request.POST.get('nome')
          pessoa.cpf= request.POST.get('cpf')
          pessoa.rg= request.POST.get('rg')
          pessoa.telefone= request.POST.get('telefone')
          pessoa.save()
          messages.success(request,'Pessoa adiconado com sucesso')
          return redirect('/list_pessoas')

def delete_pessoa(request,pk):
     pessoa = Pessoa.objects.get(id=pk)
     pessoa.delete()
     messages.success(request, "Pessoa deletada com Sucesso")
     return redirect('/list_pessoas')

def create_alugar(request):
     pessoas = Pessoa.objects.all()
     imoveis = Imovel.objects.all()
     aluguel = Aluguel()
     if request.method == "GET":
          return render(request,'aluguel/alugar.html',{'pessoas':pessoas, 'imoveis':imoveis,'aluguel':aluguel})
     else:
          aluguel.imovel = imoveis.get(id = request.POST['imovel'])
          aluguel.pessoa = pessoas.get(id =request.POST['pessoa'])
          aluguel.apartamento= request.POST.get('apartamento')
          aluguel.valor_aluguel= request.POST.get('valor_aluguel')
          aluguel.valor_multa= request.POST.get('valor_multa')
          aluguel.valor_agua= request.POST.get('valor_agua')
          aluguel.valor_luz= request.POST.get('valor_luz')
          aluguel.save()
          return redirect('/list_pessoas')

def edit_alugar(request,pk):
     aluguel = Aluguel.objects.get(id=pk)
     pessoas = Pessoa.objects.all()
     imoveis = Imovel.objects.all()

     return render(request,'aluguel/alugar.html',{'pessoas':pessoas, 'imoveis':imoveis,'aluguel':aluguel})

def list_alugueis(request):
     alugueis= Aluguel.objects.all()
     return render(request,'aluguel/list_alugueis.html',{'alugueis':alugueis})

def delet_alugel(request,pk):
     aluguel=Aluguel.objects.get(id=pk)
     aluguel.delete()
     return redirect('/list_alugueis')