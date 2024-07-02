from django.contrib import admin
from carros.models import Car, Brand


class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model',)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)




"""
Aqui podemos configurar as informações que podem ser acessadas dentro do meu admin do Django.

Um exemplo disso é na criação de tabelas no banco de dados, 


LISTDISPLAY - Campos que serão mostrados da tabela
SEARCH_FIELDS - Campos que será possivel realizar buscas 

# Usado para registrar essa implementação
admin.site.register(NOME_TABELA, NOME_TABELA_ADMIN)
"""