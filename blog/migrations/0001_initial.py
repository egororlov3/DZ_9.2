# Generated by Django 5.1.1 on 2024-09-29 15:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='заголовок')),
                ('slug', models.CharField(max_length=200, unique=True)),
                ('content', models.TextField(verbose_name='содержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='blog_previews/', verbose_name='превью (изображение)')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата создания')),
                ('is_published', models.BooleanField(default=False, verbose_name='признак публикации')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='количество просмотров')),
            ],
        ),
    ]
