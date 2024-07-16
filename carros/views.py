from django.shortcuts import render
from django.http import HttpResponse
from carros.models import Car


def cars_views(request):
 cars = Car.objects.all().order_by('factory_year')
 search = request.GET.get('search')

 if search:      
       cars = Car.objects.filter(model__icontains=search).order_by('factory_year')

 return render(
        request, 
        'index.html',
        {'cars': cars}
        )





##  cars = Car.objects.filter(brand__name='Ferrari')
## Nesse caso o a nossa busca por marca teria que ser por id por se tratar de uma chave estrangeira, nesse caso a cima usei '__' para pegar o nome do campo de carros