# Generated by Django 3.2.8 on 2021-11-26 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistance_app', '0003_auto_20211126_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assistancetype',
            name='detail',
        ),
        migrations.AlterField(
            model_name='assistance',
            name='assistance_given_date',
            field=models.DateField(null=True, verbose_name='Assistance Given Date'),
        ),
    ]