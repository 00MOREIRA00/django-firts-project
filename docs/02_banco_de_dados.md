## Model e Admin

Um model é a fonte única e definitiva de informações sobre seus dados. Ele contém os campos e comportamentos essenciais dos dados que você está armazenando. Geralmente, cada modelo é mapeado para uma única tabela de banco de dados.

Podemos criar nossas tabelas que usaremos no nosso projeto.
```
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

     # Para retornar o objeto 
        def __str__(self) -> str:
            Jaereturn self.model
```
Após criar, o orm que é utilizado no Djando irá realizar os processos ligados ao banco de dados, que nesse caso é a criação.

Agora rodamos o comando makemigrations e migrate para adicionar essa nova tabela.

### Principais comandos de migração

1. Criando migração
```
python manage.py makemigrations
```

2. Aplicar Migrações 
```
python manage.py migrate
```

3. Especificar migração de um App 
```
python manage.py makemigrations nome_do_app
```

4. Verificar status de migração
```
python manage.py showmigrations
```

5. Reverter migração
```
python manage.py migrate nome_do_app número_da_migração
```

6. Revertendo todas as migrações   
```
python manage.py migrate nome_do_app zero
```

### Tabelas para Admin

Para possibilitar adicionar o banco de dados ao admin, é necessário que venhamos habilitar no arquivo admin.

Primeiramente precisaremos criar uma class de admin para aquela tabela:
```
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model',)



# list_display - campos que serão mostrados no admin
# search_fields - campos que serão possiveis serem usados para busca
```

Depois faremos registro dele no arquivo
```
admin.site.register(Car, CarAdmin)

# Usado para registrar essa implementação
admin.site.register(NOME_TABELA, NOME_TABELA_ADMIN)
```



> Configurações do Django Admin - Dentro de settings é só modificar o "LANGUAGE_CODE" para "pt-br"

> Modificando Time Zone - TIME_ZONE = 'America/Sao_Paulo'


### Trabalhando com Chave Estrangeira

Podemos ao invés de ter que escrever um campo, fazer referência a valores de outra tabela. Exemplo: para o campo marcas da tabela carros, pegar marcas cadastradas na tabela marcas.

```
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
    value = models.FloatField(blank=True, null=True)

    # Para retornar o objeto 
    def __str__(self) -> str:
        return self.model
```

### Armazenando imagem

Como ferramenta nativa do Django, ele armazena uma referência de onde o arquivo está sendo guardado.
```
photo = models.ImageField(upload_to='cars/', blank=True, null=True)
```

Adicionar isso no settings e importar o os
```
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

No url devemos importar arquivos e adicionar esse path
````
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```