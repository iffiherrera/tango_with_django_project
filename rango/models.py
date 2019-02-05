from django.db import models

# Create your models here.
class Category(models.Model): # defining the parameters of the Category class
    name = models.CharField(max_length=128, unique=True) #PK

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


# 1:M relation category to page 

class Page(models.Model): # defining the parameters of the Page class
    category = models.ForeignKey(Category) # category is a FK of Page
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self): # generates a string representation like toString, no need for unicode as using Python3
        return self.title