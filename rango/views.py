from django.shortcuts import render

from django.http import HttpResponse 
# calling the http connecting object module.
def index(request): # the view created now is an index, it must be called request.
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcakes!"}
    # return a rendered response to send to the client
  #  return HttpResponse("Rango says hey there partner!")
    return render(request, 'rango/index.html', context=context_dict)
