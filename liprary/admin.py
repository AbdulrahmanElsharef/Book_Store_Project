from django.contrib import admin
from .models import Book , cateogry


class lipraryAdmin(admin.ModelAdmin):
    list_display=['title','author']
    list_filter=['cateogry','author']
    search_fields=['details','title']
# Register your models here.
admin.site.register(Book,lipraryAdmin)
admin.site.register(cateogry)