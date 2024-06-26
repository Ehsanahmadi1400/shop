# Generated by Django 4.2 on 2024-04-13 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_alter_product_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttype',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='catalogue.brand'),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='catalogue.category'),
        ),
        migrations.AlterField(
            model_name='productattributevalue',
            name='attribute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='attribute_values', to='catalogue.productattribute'),
        ),
    ]
