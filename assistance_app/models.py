from django.db import models


class Assistance(models.Model):
    id = models.IntegerField(max_length=10, verbose_name='ID', primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Name')
    remark = models.CharField(max_length=255, verbose_name='Remark')
    progress_percentage = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='Progress Percentage')
    victim_number = models.IntegerField(max_length=5, verbose_name='Victim Number')
    is_approved = models.BooleanField(verbose_name='Is Approve')
    user_id = models.IntegerField(max_length=5, verbose_name='User ID')
    assistance_type_id = models.IntegerField(max_length=5, verbose_name='Assistance Type ID')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Updated at')


class Assistance_type(models.Model):
    id = models.IntegerField(max_length=10, verbose_name='ID', primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Name')
    description = models.CharField(max_length=255, verbose_name='Description')
    detail = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Detail')
    assistance_given_date = models.IntegerField(max_length=8, verbose_name='Assistance Given Date')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Updated at')









