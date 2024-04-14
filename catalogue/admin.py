from django.contrib import admin
from django.contrib.admin import register

from catalogue.models import Product, ProductType, ProductAttribute, ProductAttributeValue, Brand, Category


class ProductAttributeInline(admin.StackedInline):
    model = ProductAttribute
    extra = 1


@register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['upc', 'product_type', 'title', 'category', 'brand', 'is_active']
    list_filter = ('is_active', )

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request, obj=None):
        return True

    
@register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ['title', 'product_type', 'attribute_type']


@register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    inlines = [ProductAttributeInline]


admin.site.register(Brand)
admin.site.register(Category)
