# Generated by Django 3.2.8 on 2021-11-27 06:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.IntegerField(max_length=10, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=255, verbose_name='Address1')),
                ('address2', models.CharField(max_length=255, verbose_name='Address2')),
                ('city', models.CharField(max_length=255, verbose_name='City')),
                ('mukim', models.CharField(max_length=255, verbose_name='Mukim')),
                ('parlimen', models.CharField(max_length=255, verbose_name='Parlimen')),
                ('state', models.CharField(max_length=255, verbose_name='State')),
                ('poskod', models.IntegerField(max_length=5, verbose_name='Poskod')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('ic', models.IntegerField(max_length=12, primary_key=True, serialize=False, verbose_name='IC')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('phone', models.IntegerField(max_length=5, verbose_name='Phone Number')),
                ('is_kir', models.BooleanField(default=True, verbose_name='Ketua Isi Rumah')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Salary')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='victim_app.address', verbose_name='Address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]