# Generated by Django 3.2.4 on 2021-06-14 00:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mcq_bank', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='quizsession',
            name='answers',
            field=models.ManyToManyField(blank=True, related_name='quiz_sessions', to='mcq_bank.Answer'),
        ),
        migrations.AddField(
            model_name='quizsession',
            name='questions',
            field=models.ManyToManyField(blank=True, related_name='quiz_sessions', to='mcq_bank.Question'),
        ),
        migrations.AddField(
            model_name='quizsession',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_sessions', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mcq_bank.category', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='question',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='mcq_bank.category', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ManyToManyField(blank=True, related_name='questions', to='mcq_bank.Quiz', verbose_name='Quiz'),
        ),
        migrations.AddField(
            model_name='question',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mcq_bank.subcategory', verbose_name='Sub-Category'),
        ),
        migrations.AddField(
            model_name='history',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='mcq_bank.question', verbose_name='Question'),
        ),
    ]