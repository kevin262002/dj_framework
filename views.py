'''from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def members(request):
    return HttpResponse("Hello")'''
    
'''from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('my_data.html')
  return HttpResponse(template.render())    '''
  
from django.http import HttpResponse
from django.template import loader

def members(request):
    template = loader.get_template('my_data.html')
    return HttpResponse(template.render())  
  