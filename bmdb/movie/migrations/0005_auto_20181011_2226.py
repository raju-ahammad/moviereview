# Generated by Django 2.1.2 on 2018-10-11 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_auto_20181010_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('HO', 'Hollywood'), ('BO', 'BollyWood'), ('IB', 'Indian_bangla'), ('TA', 'Tamil'), ('IO', 'Indian_others'), ('BA', 'Bangladesh'), ('FO', 'Foreign')], default='HO', max_length=120),
        ),
    ]
