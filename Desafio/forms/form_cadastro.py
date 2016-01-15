#coding: utf-8 

from django import forms

class Form_Cadastro(forms.Form):
	
	tarefa = forms.CharField(
		max_length=100,
		widget=forms.TextInput(attrs={
			'class':'form-control',
			'placeholder':'Informe a tarefa...',
			'id':'tarefa'
		})
	)	