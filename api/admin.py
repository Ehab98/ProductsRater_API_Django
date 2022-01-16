from re import search
from django.contrib import admin
from .models import Product , Rating
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=['id', 'name','description']
    search_field = ['name', 'description']
    list_filter = ['name']

class RatingAdmin(admin.ModelAdmin):
    list_display=['id','product','user','stars']
    list_filter= ['product','user']


admin.site.register(Product,ProductAdmin)

admin.site.register(Rating,RatingAdmin)