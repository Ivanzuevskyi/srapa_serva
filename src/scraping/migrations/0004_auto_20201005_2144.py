# Generated by Django 3.0.10 on 2020-10-05 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0003_vacancy'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacancy',
            options={'verbose_name': 'Вакансия', 'verbose_name_plural': 'Вакансии'},
        ),
    ]
