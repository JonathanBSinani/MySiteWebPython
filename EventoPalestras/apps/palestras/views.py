from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index_palestras(request):
	return HttpResponse("sou a página principal de palestras")
