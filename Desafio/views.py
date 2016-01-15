# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator
from Desafio.models import Logs, Tarefas
from Desafio.forms.form_cadastro import Form_Cadastro
from datetime import date

def home(request):
	return render(request, 'index.html')

def cadastra_tarefa(request):

	if request.method == 'POST':
		form = Form_Cadastro(request.POST)

		if form.is_valid():
			tarefa = Tarefas()
			tarefa.tarefa = request.POST["tarefa"]
			tarefa.situacao = False
			tarefa.save()

			log = Logs()
			log.acao = "Insercao"
			log.data = date.today()
			log.objeto = tarefa.tarefa
			log.save()

		return redirect("/lista_tarefas/")

	else:
		form = Form_Cadastro()

	return render(request, 'cadastra_tarefa.html', {
		"cadastra_tarefa":form,
	})

def lista_tarefas(request):

	tarefa = Tarefas.objects.all().order_by('situacao')

	paginator = Paginator(tarefa, 5)

	try:
		page = int(request.GET.get('page', 1))
	except:
		page = 1

	try:
		tarefas_page = paginator.page(page)
	except:
		tarefas_page = paginator.page(paginator.num_pages)

	return render(request, 'lista.html', {
		'tarefas': tarefas_page,
	})

def exclui_tarefa(request, id):

	tarefa = Tarefas.objects.get(pk=id)

	log = Logs()
	log.acao = "Marcando tarefa como Concluída"
	log.data = date.today()
	log.objeto = id
	log.save()

	tarefa.situacao = True
	tarefa.save()
	
	return redirect('/lista_tarefas')

