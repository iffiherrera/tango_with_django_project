from django.contrib import admin
from rango.models import Category, Page

# Register your models here.
admin.site.register(Category)
admin.site.register(Page)

# Add more classes just do as above admin.site.register(NAMEOFCLASS)