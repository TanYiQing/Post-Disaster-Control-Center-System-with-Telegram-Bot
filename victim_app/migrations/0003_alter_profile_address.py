# Generated by Django 3.2.8 on 2021-12-05 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('victim_app', '0002_auto_20211127_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='victim_app.address', verbose_name='Address'),
        ),
    ]
