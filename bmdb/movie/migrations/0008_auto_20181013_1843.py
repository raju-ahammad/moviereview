# Generated by Django 2.1.2 on 2018-10-13 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie', '0007_auto_20181011_2315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Movie')),
            ],
        ),
        migrations.AlterField(
            model_name='genera',
            name='name',
            field=models.CharField(choices=[('Action', 'Action'), ('Sci-Fi', 'Sci-Fi'), ('Drama', 'Drama'), ('Adventure', 'Adventure'), ('Romantic', 'Romantic'), ('Horor', 'Horor'), ('Thriller', 'Thriller')], default='Action', max_length=120),
        ),
    ]
