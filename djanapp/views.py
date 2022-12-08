from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    #             запрос    папка     файл    параметр ключ   значение       
    return render(request, 'djanapp/home.html')
    
    
def about(request):
    #             запрос    папка     файл    параметр ключ   значение       
    return render(request, 'djanapp/about.html')

def simple(request):
    #             запрос    папка     файл    параметр ключ   значение       
    return render(request, 'djanapp/simple.html')