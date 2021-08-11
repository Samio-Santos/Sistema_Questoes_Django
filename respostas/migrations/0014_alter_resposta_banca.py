# Generated by Django 3.2 on 2021-05-27 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
        ('respostas', '0013_resposta_banca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resposta',
            name='banca',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categorias.banca'),
        ),
    ]