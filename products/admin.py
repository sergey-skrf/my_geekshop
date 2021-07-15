from django.contrib import admin

from products.models import ProductCategory, Product

#admin.site.register(Product)
admin.site.register(ProductCategory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'image', 'description', 'category', ('price', 'quantity'))
    readonly_fields = ('description',)
    ordering = ('quantity',)
    search_fields = ('name',)
