Esse arquivo deve ser ignorado. Usado apenas como nota. 
E em caso de não desejar utilizar o Docker.


# Configuração PostgreSQL no Django

Em BudgetManager/settings.py, substituir a variável DATABASES

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': <nome-do-seu-banco>,
        'USER': <nome-do-user>,
        'PASSWORD': <nome-da-password>,
        'HOST': <db-hostname-ou-ip>, # Por estar configurado localmente vai ser no localhost ou 127.0.0.1
        'PORT': <porta-do-banco> # Por padrão o PostgreSQL roda na porta 5432
    }
}

# Criando um banco de dados Postgres

Abrir o terminal e digitar os seguintes comandos:

sudo -i -u postgres
psql
CREATE USER 'usuário' WITH PASSWORD 'senha';
CREATE DATABASE 'nomedoseubanco';
ALTER DATABASE 'nomedoseubanco' OWNER TO 'seuusuário';

o nome do seu banco, seu usuário e senha serão usados no arquivo .env
