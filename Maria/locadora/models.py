from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome 
    
class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.nome
    
class Locacao(models.Model):
    nome = models.CharField(max_length=200)
    data = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True,null=True)

    def __str__(self):
        return self.nome
    
class Filmes(models.Model):
    titulo = models.CharField(max_length=200)
    valor = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=True,null=True)
    locacao = models.ManyToManyField(Locacao)

    def __str__(self):
        return self.titulo


