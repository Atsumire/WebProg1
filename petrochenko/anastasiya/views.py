from django.shortcuts import render
from django.http import HttpResponse	
  
def myname(request):
 	return HttpResponse("<h1>Петроченко Анастасия</h1>")

def mygroup(request):
    return HttpResponse("<h1>БИН-22-2</h1>")

def myage(request):
    return HttpResponse("<h1>22</h1>")

def mycommon(request):
    return HttpResponse("<h1>Петроченко Анастасия</h1><h2>Группа: БИН-22-2</h2><h2>Возраст: 22</h2>")