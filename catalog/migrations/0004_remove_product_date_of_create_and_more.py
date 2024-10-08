# Generated by Django 5.1.1 on 2024-09-25 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_category_alter_product_category_delete_categoy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='date_of_create',
        ),
        migrations.RemoveField(
            model_name='product',
            name='last_changes',
        ),
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='дата создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='дата последнего изменения'),
        ),
    ]
