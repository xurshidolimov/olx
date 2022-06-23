from django.contrib import admin

from pages.models import Product, Category, Likes

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Likes)