# Generated by Django 5.0.6 on 2024-06-19 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='media/blog', verbose_name='Изображение'),
        ),
    ]
