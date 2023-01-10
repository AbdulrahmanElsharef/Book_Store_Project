from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=25)
    details = models.TextField(max_length=500)
    slug = models.SlugField(null=True, blank=True)
    cateogry = models.ForeignKey(
        'cateogry', on_delete=models.CASCADE, related_name='cateogry')
    image = models.ImageField(upload_to='liprary/images')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)


class cateogry(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
