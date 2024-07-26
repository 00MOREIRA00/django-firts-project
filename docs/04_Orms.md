# Orms

Alggo que devemos ter em mente é que o arquivo de Views ele, baseicamente tem como objetivo trabalhar com logica, dessa forma após ter essa logica ele chama o template. Desse forma quando vamos conversar com o Banco de Dados, temos uma conversa entre o arquivo View e o arquivo de Models.

> O Django p ossui um ORM proprio para trabalhar, dessa forma não possuindo necessidade de utilizar um sqlalchemy por exemplo.

### Dados do Banco

Nesse exxmplo iremos trabalhar com os dados do Banco de Dados para serem mostrados no template.

Primeira coisa que fazemos é uma modificação na view que irá fazer uma comunicação com o Banco de Dados.
```
Fizemos uma modificação onde usamos o o orme do Djnago para pegar tudo do banco e adiconamos no content.

from carros.models import Car
def cars_views(request):
 cars = Car.objects.all()

 return render(
        request, 
        'index.html',
        {'cars': cars}
        )


Depois nós criamos um for para pegar todas essas informações

 {% block content %}
  <body>
    {% for car in cars %}
      <h3>{{ car.model }}</h3>
    {% endfor %}
  </body>
  {% endblock %}
```

### Executando Querys Intelientes 


```
def cars_views(request):
 #cars = Car.objects.all()
 cars = Car.objects.filter(model='Fox')


 return render(
        request, 
        'index.html',
        {'cars': cars}
        )
```

```
##  cars = Car.objects.filter(brand__name='Ferrari')
## Nesse caso o a nossa busca por marca teria que ser por id por se tratar de uma chave estrangeira, nesse caso a cima usei '__' para pegar o nome do campo de carros
```

```
Executando pesquisa por conter a palavra em especifico

cars = Car.objects.filter(model__contains='Fox')
```

### Capturando parametro da QueryString

```
link da chamada: 127.0.0.1:8000/cars/?search=Teste&nome=Francisco

def cars_views(request):
 print(request.GET.get('search'))
 print(request.GET.get('nome'))
 cars = Car.objects.all()
 #cars = Car.objects.filter(model__contains='F')


 return render(
        request, 
        'index.html',
        {'cars': cars}
        )

```


### Buscando por parametro

```
def cars_views(request):
 print(request.GET.get('search'))
 #print(request.GET.get('nome'))
 cars = Car.objects.filter(model__contains=request.GET.get('search'))
 #cars = Car.objects.filter(model__contains='F')


 return render(
        request, 
        'index.html',
        {'cars': cars}
        )


# EXEMPLO MAIS COMPLETO
def cars_views(request):
 cars = Car.objects.all()
 search = request.GET.get('search')

 if search:      
       cars = Car.objects.filter(model__contains=search)

 return render(
        request, 
        'index.html',
        {'cars': cars}
        )
```

> Usar o icontains é melhor pois ele ignora se as letras estão em caixa alto ou baixa.

> Podemos utilizar um 'order_by' para ordenar a pesquisa
```
cars = Car.objects.all().order_by('factory_year')

Para inverter a organização só adicionar um -

cars = Car.objects.all().order_by('-factory_year')
```




```
Nesse caso chamamos o "cars_list" que é a url de carros, mas agora com o atributo name atribuido la no urls

<form method="GET" action="{% url 'cars_list' %}">
      <input type="text" name="search" placeholder="Buscar Carro...."/>
      <button type="submit">Buscar</button>
</form>




> Arquivo URLs
urlpatterns = [
    path('admin/', admin.site.urls),
     path('cars/', cars_views, name='cars_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```


```
Usando a Django Template language podemos fazer uma verificação se temos algum resultado para retornar html customizado

    <div>
        {% if cars %}
          {% for car in cars %}
          <h3>{{car.brand}} - {{ car.model }} - {{car.factory_year}}</h3>
        {% endfor %}
        {% else %}
          <p>Carro não encontrado</p>
        {% endif %}
    </div>


Onde se tivemos a busca dentro do cars ele retorna, e caso contario, irá retornar o "Carro não encontrado"
```


#### Usando template Base

Criamos nosso arquivo base html com todos os elementos html que queremos que seja utilizado em todo o projeto, e após iremos ao arquivo settings conde cadastraremos o local onde se encontra nossa pasta de tamplates.

```
Na parte de tamplates nós informamos o diretorio

'DIRS': ['app/templates'],
```

