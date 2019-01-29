from django.shortcuts import render

from django.http import HttpResponse 
# calling the http connecting object module.
def index(request): # the view created now is an index, it must be called request.
    return HttpResponse("Rango says hey there partner!")
