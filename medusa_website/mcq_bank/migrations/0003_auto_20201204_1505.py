# Generated by Django 3.1.3 on 2020-12-04 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mcq_bank', '0002_answer_is_correct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='mcq_bank.question'),
        ),
    ]