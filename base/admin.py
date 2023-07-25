from django.contrib import admin
from .models import Product, Orders, Category

admin.site.register(Category)
admin.site.register(Orders)
admin.site.register(Product)


