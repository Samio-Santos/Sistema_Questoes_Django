# Generated by Django 3.2 on 2021-06-05 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210605_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='costumeruser',
            name='sexo',
            field=models.CharField(blank=True, default=None, max_length=15, null=True),
        ),
    ]
