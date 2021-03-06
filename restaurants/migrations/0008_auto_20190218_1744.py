# Generated by Django 2.1.5 on 2019-02-18 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='restaurant',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.AlterField(
            model_name='favoriterestaurant',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favs', to='restaurants.Restaurant'),
        ),
        migrations.AlterField(
            model_name='favoriterestaurant',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
