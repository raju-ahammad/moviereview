# Generated by Django 2.1.2 on 2018-10-10 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20181010_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='plot',
            field=models.TextField(blank=True, max_length=400),
        ),
    ]
