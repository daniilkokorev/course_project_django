# Generated by Django 5.0.6 on 2024-06-14 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0002_alter_mailingsettings_last_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailingstatus',
            name='status',
            field=models.CharField(choices=[('success', 'Успешно'), ('error', 'Ошибка')], default='', max_length=50, verbose_name='status'),
        ),
    ]