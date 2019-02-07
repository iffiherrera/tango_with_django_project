from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin): # new class for page admin attributes
    list_display = ('title','category','url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin) # ch.5 excerices adds another parameter inside page.


# Add more classes just do as above admin.site.register(NAMEOFCLASS)