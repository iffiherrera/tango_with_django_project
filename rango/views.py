from django.shortcuts import render
from rango.models import Category
from rango.models import Page

from django.http import HttpResponse 
# calling the http connecting object module.

  #Ch3  context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcakes!"}  
  #Ch3  return HttpResponse("Rango says hey there partner!")
  #Ch4 return render(request, 'rango/index.html', context=context_dict)
    
def index(request): # the view created now is an index, it must be called request.
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    # return a rendered response to send to the client
    return render(request, 'rango/index.html',context_dict)

def about(request):
    context_dict = {'boldmessage' : 'This tutorial has been put together by Ifigenia Temesio'}
    return render(request, 'rango/about.html', context=context_dict)

def show_category(request, category_name_slug):

    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    
    except Category.DoesNotExist:
        context_dict['category'] = None 
        context_dict['pages'] = None 

    return render(request, 'rango/category.html', context_dict)
