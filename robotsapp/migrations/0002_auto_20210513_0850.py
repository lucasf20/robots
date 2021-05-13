# Generated by Django 3.0.6 on 2021-05-13 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('robotsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='robo',
            name='cliente',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='robotsapp.Cliente'),
        ),
    ]
