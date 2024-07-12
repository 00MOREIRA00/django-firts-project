from django.shortcuts import render
from django.http import HttpResponse
from carros.models import Car


def cars_views(request):
 cars = Car.objects.all()

 return render(
        request, 
        'index.html',
        {'cars': cars}
        )
