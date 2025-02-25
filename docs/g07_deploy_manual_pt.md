# Catalogue Collections

# Requirements
* Python 3.5 >= (https://www.python.org)
* Django 2.0 >= (https://www.djangoproject.com)
  * Django Rest Framework 3.0 >= (http://www.django-rest-framework.org)
* PostgreSQL 9.6 >= (https://www.postgresql.org)


## Enviroment Local
### Docker
Para levantar um ambiente de desenvolvimento local do Guia IMS, basta [instalar Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/) e executar o seguinte comando na raiz do repositório:

`docker-compose up`

Para executar comandos dentro do container Django, rode `docker-compose exec django bash`. Ela vai te dar o shell interno do container, em que  você pode executar tarefas rotineiras como `python manage.py makemigrations` e `python manage.py migrate` (este último comando sempre é executado quando os containers se levantam, então não é necessário avisar outros desenvolvedores sobre a presença de novas migrações).

#### Diretórios estáticos locais (ignorados pelo Git)
- `media` - arquivos enviados pelos usuários
- `db_data` - dados de banco de dados do Postgres. Para apagar todos os dados do banco, basta deletar essa pasta

#### Variáveis de ambiente
Um exemplo funcional das variáveis de ambiente necessárias para rodar a aplicação é continuamente mantido no arquivo `env.example` para referência de desenvolvedores e operadores de infraestrutura.

## Enviroment Deploy
> Exemplos construídos em torno de um servidor Debian 9 e/ou Ubuntu 16.04.

### 1. Server Dependencies

##### 1.1. GIT Install
```
# apt-get install git
```
##### 1.2. PostgreSQL e Postgis
Recomendamos o postgreSQL, mas o django suporta outros bancos de dados relacionais.
```
# apt install postgresql postgresql-contrib postgis postgresql-9.6-postgis-2.3 postgresql-9.6-postgis-2.3-scripts
```

##### 1.3. GDAL

```
apt-get install gdal-bin libgdal-dev libgdal-doc libgdal-grass python3-gdal
```

##### 1.4. Python3, PIP & virtualenv
```
# apt update
# apt install python3 build-essential python3-dev gettext python-virtualenv gcc
# echo "alias python=python3" >> ~/.bashrc
```
verifique se possui o pip instalado:
```
$ pip --version
```
Instalação: https://pip.pypa.io/en/stable/installing/

Instale o virtualenv
```
# pip install virtualenv
```

### 2. Python Package Dependencies

##### 2.1. virtualenv

Crie o env:

```
$ virtualenv env
```

Ative o env:
```
$ source env/bin/activate
```

Desative o env se necessário:

```
$ deactivate
```

##### 2.2. Django
Esse comando deve ser dado com env ativado e sem sudo. Se for exigido root, há problema na identificação de enviroment. Isso pode ser corrigido mudando o path do env.

```
$ pip install django
```

##### .env
Crie um arquivo .env na raiz da aplicação e preencha com as seguintes informações:
```
URL=localhost
DEBUG=True
SECRET_KEY=YourSecretHere
DB_NAME=YourDataBase
DB_USER=YourUserDB
DB_PASSWORD=YourPasswordDatabse
DB_HOST=YourHostExLocalhost
#COMMENTED=Some comment
```
Referencia: https://pypi.org/project/python-decouple/#where-the-settings-data-are-stored

### 3. Database

##### 3.1. User database e banco

```
# sudo su - postgres -c "createuser -d guia"
```

Caso precise trocar a senha do usuário:
```
psql=> ALTER USER guia WITH PASSWORD 'passwordguia';
```

Com usuário da aplicação - logado como **guia** - crie a base de dados
```
psql=>
```

ou com usuário postgres:

```
postgres@server$ createdb --encoding "UTF-8" guia
```

Caso precise dar privilegios:

```
postgres# psql guia -c "GRANT all privileges on DATABASE guia TO guia WITH GRANT OPTION;"
postgres# psql guia -c "GRANT ALL ON ALL TABLES IN SCHEMA public to guia;"
postgres# psql guia -c "GRANT ALL ON ALL SEQUENCES IN SCHEMA public to guia;"
postgres# psql guia -c "GRANT ALL ON ALL FUNCTIONS IN SCHEMA public to guia;"
```

Para usar campos postgis, como super user você deve aplicar:
```
postgres@server$ psql
postgres=# \c guia
guia=# CREATE EXTENSION IF NOT EXISTS postgis;
```

##### 3.2. Django Database
```
python3.5 manage.py makemigrations
$ python3.5 manage.py migrate
```

##### 3.3 Importando e exportando dados

Para exportar dados:

```
$ python manage.py dumpdata > data.json
```

Para importar dados:

```
$ python manage.py loaddata data.json
```

## Atalhos

### Rodando a aplicação localmente
1. Ative o env
2. Rode o runserver
```
$ python3.5 manage.py runserver
```

### References
* UWSGI
  * https://docs.djangoproject.com/pt-br/2.0/howto/deployment/wsgi/uwsgi/
