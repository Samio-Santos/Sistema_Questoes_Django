# Generated by Django 3.2 on 2021-05-26 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perguntas', '0013_pergunta_alternativas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pergunta',
            name='alternativas',
            field=models.JSONField(default={}),
        ),
    ]
