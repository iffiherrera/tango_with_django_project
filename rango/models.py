from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Category(models.Model): # defining the parameters of the Category class
    name = models.CharField(max_length=128, unique=True) #PK
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category,self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'categories'

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

class UserProfile(models.Model):
    user = models.OneToOneField(User) # uses the default 5 fields.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


