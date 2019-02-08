from django.shortcuts import render
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm
from rango.forms import PageForm

from django.http import HttpResponse 
# calling the http connecting object module.

  #Ch3  context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcakes!"}  
  #Ch3  return HttpResponse("Rango says hey there partner!")
  #Ch4 return render(request, 'rango/index.html', context=context_dict)
    
def index(request): # the view created now is an index, it must be called request.
    category_list = Category.objects.order_by('-likes')[:5]
    pages_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list,
                    'pages': pages_list}
    
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

def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
           category = form.save(commit=True) # save valid form and confirmation message.
            # return to home page.
        return index(request)

    else:
        print(form.errors) # error message, if no form or bad form.
    return render(request, 'rango/add_category.html', {'form': form})

def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return show_category(request, category_name_slug)
        else:
            print(form.errors)
    
    context_dict = {'form':form, 'category':category}
    return render(request, 'rango/add_page.html', context_dict)
        