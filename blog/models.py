from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super(Category, self).save(*args, **kwargs)



    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='posts/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    






