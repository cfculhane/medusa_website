# Generated by Django 3.2.4 on 2021-06-06 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mcq_bank', '0006_auto_20210405_1710'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Progress',
            new_name='History',
        ),
        migrations.AlterModelOptions(
            name='history',
            options={'verbose_name': 'User History', 'verbose_name_plural': 'User progress records'},
        ),
        migrations.AddField(
            model_name='quizsession',
            name='history',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='mcq_bank.history'),
        ),
    ]