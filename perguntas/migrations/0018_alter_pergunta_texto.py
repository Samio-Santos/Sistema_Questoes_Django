# Generated by Django 3.2 on 2021-06-12 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perguntas', '0017_pergunta_texto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pergunta',
            name='texto',
            field=models.TextField(blank=True, null=True),
        ),
    ]
