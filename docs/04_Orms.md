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