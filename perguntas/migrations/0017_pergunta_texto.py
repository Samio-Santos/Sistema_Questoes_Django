# Generated by Django 3.2 on 2021-06-10 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perguntas', '0016_auto_20210526_0753'),
    ]

    operations = [
        migrations.AddField(
            model_name='pergunta',
            name='texto',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
