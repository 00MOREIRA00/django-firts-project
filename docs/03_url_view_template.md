# Url, Views e Templates

Url - são as rotas que iremos defenir para quando foi inserido url possa direcionar para cada funcionalidade 



Url  ->  View  ->  Template





### Mocando View para testes 

Identifiquei que como padrão, alguns usuários para testarem algumas lógicas de desenvolvimento, colocam suas views direto no arquivo url Como por exemplo:
```
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

def cars_views(request):
 return HttpResponse('Meus carros')

urlpatterns = [
    path('admin/', admin.site.urls),
     path('cars/', cars_views),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

> Dessa forma podemos ver ser a lóica funciona antes de estruturar


Para o funcionamento dessa renrediração de telas temos três atores que funcionam ativamente.

1. Arquivo url:  Nesse arquivo temos a criaçã das urls que serãoo chamadas durante a utilização. Com ela atribuimos uma view e um nome para ela.
2. View: Nesse arquivo temos lógicas, renderizações, interação coom modeloos. Dentre outras coisas
3. Template: Local onde fica armazenadoo os códigos html para utilização. 



### Templates

Recomenda-se que tenhamos uma pasta chamada de templates para receber nossas páginas  que serão criados para o projeto.


### View

* Context é usado para trabalhar com dados. Exemplo:

```
Tenho essa view que recebe "cars" em seu context

def cars_views(request):
 return render(
        request, 
        'index.html',
        {'cars': {'model': 'Astra 2.0'}}
        )



Com ele posso trabalhar no meu html
{% block content %}
  <body>
    <h3>{{ cars.model }}</h3>

  </body>
  {% endblock %}
```
