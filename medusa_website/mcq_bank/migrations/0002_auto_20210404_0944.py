# Generated by Django 3.1.6 on 2021-04-03 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcq_bank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='url',
            field=models.CharField(help_text='a user friendly url', max_length=60, verbose_name='user friendly url'),
        ),
    ]
