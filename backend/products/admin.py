from django.contrib import admin

# Register your models here.
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_filter = ('title', 'content')
    list_display = ('title', 'content', 'price', 'public', 'user')


admin.site.register(Product, ProductAdmin)
