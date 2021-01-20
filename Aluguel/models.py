from django.db import models
# Create your models here.
class Imovel( models.Model):
    cep = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.endereco

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=10)
    telefone = models.CharField(max_length=12)
    nascimento = models.DateField()
    def __str__(self):
        return self.nome

class Aluguel(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    apartamento = models.CharField(max_length=200)
    valor_aluguel = models.CharField(max_length=10)
    valor_multa = models.CharField(max_length=10)
    valor_agua = models.CharField(max_length=10)
    valor_luz = models.CharField(max_length=10)
    data_ingresso = models.DateField()

    def __str__(self):
        return str(self.pessoa) + ', '+str(self.apartamento)

class Boleta(models.Model):
    data_boleta_inicio= models.DateField()
    data_boleta_final= models.DateField()
    aluguel = models.ForeignKey(Aluguel,on_delete=models.CASCADE)
    
    def __str__(self) :
        return str(self.aluguel.pessoa) +\
        ' ,'+str(self.aluguel.imovel)+\
      ' , bolete DE '+str(self.data_boleta_inicio)+' A '+str(self.data_boleta_final)