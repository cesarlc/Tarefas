# -*- coding: utf-8 -*-
from django.db import models

class Tarefas(models.Model):
    tarefa = models.CharField(max_length=100)
    situacao = models.BooleanField()

    def __unicode__(self):
        return self.nome

class Logs(models.Model):
    acao = models.CharField(max_length=50)
    data = models.DateField()
    objeto = models.CharField(max_length=100)

    def __unicode__(self):
        return self.acao

