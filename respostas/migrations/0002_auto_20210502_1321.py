# Generated by Django 3.2 on 2021-05-02 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('respostas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resposta',
            old_name='resposta',
            new_name='resposta_pergunta',
        ),
        migrations.AddField(
            model_name='resposta',
            name='data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='resposta',
            name='resposta_certa',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resposta',
            name='resposta_errada',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resposta',
            name='usuario',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.costumeruser'),
            preserve_default=False,
        ),
    ]