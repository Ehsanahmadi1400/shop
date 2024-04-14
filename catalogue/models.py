from django.db import models


class ProductType(models.Model):
    title = models.CharField(max_length=32, blank=True, null=True, verbose_name='title')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"


class ProductAttribute(models.Model):

    INTEGER = 1
    STRING = 2
    FLOAT = 3

    ATTRIBUTE_TYPES = [
        (INTEGER, 'Integer'),
        (STRING, 'String'),
        (FLOAT, 'Float' ),
    ]
    title = models.CharField(max_length=32)
    product_type = models.ForeignKey(ProductType, related_name='attributes', on_delete=models.CASCADE)
    attribute_type = models.PositiveSmallIntegerField(choices=ATTRIBUTE_TYPES, default=INTEGER)

    def __str__(self):
        return f"{self.title}"


class Category(models.Model):

    title = models.CharField(max_length=32)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        # db_table = category_table

    def __str__(self):
        return f"{self.title}"


class Brand(models.Model):

    title = models.CharField(max_length=32)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)

    def __str__(self):
        return f"{self.title}"


class Product(models.Model):

    title = models.CharField(max_length=32)
    upc = models.BigIntegerField(unique=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT, related_name='products')
    description = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True)

    category = models.ForeignKey(Category, related_name='products', on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.title}"


class ProductAttributeValue(models.Model):

    value = models.CharField(max_length=48)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='attribute_values')
    attribute = models.ForeignKey(ProductAttribute, on_delete=models.PROTECT, related_name='attribute_values')

    def __str__(self):
        return f"{self.product} {self.attribute} {self.value}"
