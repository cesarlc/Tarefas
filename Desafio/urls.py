"""Desafio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
import Desafio.views

urlpatterns = patterns('',
	url(r'^$', 'Desafio.views.home', name='home'),
	url(r'^lista_tarefas/$', 'Desafio.views.lista_tarefas', name='lista'),
    url(r'^cadastra_tarefa/$', 'Desafio.views.cadastra_tarefa', name='cadastra'),
    url(r'^exclui_tarefa/(?P<id>\d+)/$', 'Desafio.views.exclui_tarefa', name='exclui'),
    url(r'^marca_tarefa/(?P<id>\d+)/$', 'Desafio.views.marca_tarefa', name='marca'),
)