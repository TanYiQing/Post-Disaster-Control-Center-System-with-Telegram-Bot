# Generated by Django 3.2.8 on 2021-12-09 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistance_app', '0012_alter_assistance_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assistance',
            name='progress_percentage',
            field=models.DecimalField(blank=True, decimal_places=2, default='0.0', max_digits=3, null=True, verbose_name='Progress Percentage'),
        ),
    ]
