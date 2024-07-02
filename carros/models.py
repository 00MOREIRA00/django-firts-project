from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    # Para retornar o objeto 
    def __str__(self) -> str:
        return self.name

# Car`s Data Base
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)

    # Para retornar o objeto 
    def __str__(self) -> str:
        return self.model







"""Class Model já existe pro padrão no Framework, e estamos usando coo base 

max_length - Maximo de caracteres possiveis
blank - Pode ficar em branco
null - Pode ficar nulo
on_delete - Especificar comportamento caso o dado seja deletado
related_name - Nome dado para essa relação 



"""
