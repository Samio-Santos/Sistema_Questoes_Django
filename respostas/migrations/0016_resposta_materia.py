# Generated by Django 3.2 on 2021-07-02 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('respostas', '0015_alter_resposta_banca'),
    ]

    operations = [
        migrations.AddField(
            model_name='resposta',
            name='materia',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
    ]
