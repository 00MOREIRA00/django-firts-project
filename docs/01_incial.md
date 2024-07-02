## Arquivos 

* Manage: Orquestrador do projeto;
* Settings: Todas as configurações do projeto
* Url: Para configurações de urls do projeto
* Wsgi: Para gerenciar as configurações quando deployado 



Podes ter mais de um aplicativo dentro do projeto. Por exemplo, app de Gerenciar Carros, app de Gerenciar Vendedores e app de Gerenciar Venda dentro do projeto de uma concessionaria.


## Arquivos dos Apps

* tests: Usado para a criação de testes para o app.
* app: Possui as configurações básicas sobre o app. 
* models: Aqui será escritos os modelos que serão usados.
* views: Aqui será escrito todas as views do app. Exemplo, lógicas de renderização. 
* admin: Tem relação com o Admin do Django.


## Banco de Dados

O Django nos fornece muitas estruturas já criadas para que possamos usar e facilitar nosso desenvolvimento, inclusives tabelas que podemos usar em nossos desenvolvimentos.

Migration uma forma de versionar o schema de sua aplicação. Migrations trabalha na manipulação da base de dados: criando, alterando ou removendo. Uma forma de controlar as alterações do seu banco juntamente com o versionamento de sua aplicação e compartilhar-la.

Make migrations 
```bash
python .\manage.py makemigrations
```
Inicialmente não temos nada que possa ser feito, pois não criamos nada em sql no projeto

migrate
```bash
python .\manage.py migrate
```
Ele pega todo script e roda realmente no banco de dados

Sempre que alteramos algo referente ao banco de dados no código, rodamos sempre o make migration e depois o migrate para subir essa modificação no banco de dados.

O Django por si já cria alguns bancos para utilização de alguns recursos nativos do framework


* Criando um super usuário para o admin do projeto
```bash
python .\manage.py createsuperuser
```
Preenchemos as informações necessárias e criamos.