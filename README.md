# Tarefas

Para utilizar este sistema tenha:
	-Tenha o python instalado;
	-Postgres instalado;
		-Se sua senha e usu�rio do postressql for postgres, postgres respectivamente;
		-Se sua senha e usu�rio n�o for essa, modifique o arquivo setings.py:
			DATABASES = {
			    'default': {
			        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add   '',db.backends.mysql, 'sqlite3' or 'oracle'.
			        'NAME': 'desafio',                      # Or path to database file if using sqlite3.
			        # The following settings are not used with sqlite3:
			        'USER': 'seu_usu�rio',
			        'PASSWORD': 'sua_senha',
			        'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
			        'PORT': '5432',  
			    }
			}
		-Da mesma forma essa configura��o pode mudar se for feita em outro SGBD;
	-Crie um banco de dados chamado 'desafio', caso queira criar um banco de dados com outro nome
		modifique o nome na tag NAME de 'desafio' para o nome de seu banco;
	-Django 1.9;
	-Virtualenv;
	-Crie uma myenv com o comando: virtualenv nome_Virtualenv;
	-Coloque o projeto dentro da vitrualenv;
	-Entre na pasta do projeto via linha de comando e execute os seguintes comandos:
		-python manage.py makemigrations desafio;
		-python manage.py migrate desafio;
		-python manage.py runserver;
	-V� em seu navegador e digite localhost:8000