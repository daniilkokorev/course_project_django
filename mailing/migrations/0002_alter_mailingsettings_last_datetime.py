# Generated by Django 5.0.6 on 2024-06-12 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailingsettings',
            name='last_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Конец рассылки'),
        ),
    ]