from django.shortcuts import render
from django.http import HttpResponse


def cars_views(request):
 return render(
        request, 
        'index.html',
        {'cars': {'model': 'Astra 2.0'}}
        )
