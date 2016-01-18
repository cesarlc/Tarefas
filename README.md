# Desafio ItFlex

## Instalação e Execução:

1) Tenha o python instalado;
* Postgres instalado
* Se sua senha e usuário do postressql for postgres, postgres respectivamente
* Se sua senha e usuário não for essa, modifique o arquivo setings.py:


Para utilizar este sistema tenha:

1) Tenha o python instalado
* Django 1.9
* Virtualenv
* Postgres instalado
* Se sua senha e usuário do postressql for postgres, postgres respectivamente
* Se sua senha e usuário não for essa, modifique o arquivo setings.py:
* DATABASES = {
	'default': {
	'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add   '',db.backends.mysql, 'sqlite3' or 'oracle'.
	'NAME': 'desafio',                      # Or path to database file if using sqlite3.
	# The following settings are not used with sqlite3:
	'USER': 'seu_usuário',
	'PASSWORD': 'sua_senha',
	'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
	'PORT': '5432',  
	}
}
* Da mesma forma essa configuração pode mudar se for feita em outro SGBD
2) Crie um banco de dados chamado 'desafio', caso queira criar um banco de dados com outro nome
		modifique o nome na tag NAME de 'desafio' para o nome de seu banco no arquivo Settings.py
6) Crie uma myenv com o comando: virtualenv nome_Virtualenv
7) Coloque o projeto dentro da vitrualenv
8) Entre na pasta do projeto via linha de comando e execute os seguintes comandos:
* python manage.py makemigrations desafio
* python manage.py migrate desafio
* * python manage.py runserver
* Vá em seu navegador e digite localhost:8000
