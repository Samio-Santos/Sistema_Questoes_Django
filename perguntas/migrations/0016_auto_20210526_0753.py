# Generated by Django 3.2 on 2021-05-26 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perguntas', '0015_alter_pergunta_alternativas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pergunta',
            name='alternativas',
        ),
        migrations.AddField(
            model_name='pergunta',
            name='alternativas_Multiplasescolhas',
            field=models.JSONField(blank=True, default={'A': ' ', 'B': ' ', 'C': ' ', 'D': ' ', 'E': ' '}, null=True),
        ),
    ]
