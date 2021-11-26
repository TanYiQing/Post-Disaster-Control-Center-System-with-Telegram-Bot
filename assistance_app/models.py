from django.db import models
from django.contrib.auth.models import User


class AssistanceType(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Updated at')
    
    def __str__(self):
        return self.name

class Assistance(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    remark = models.TextField( verbose_name='Remark')
    progress_percentage = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='Progress Percentage')
    victim_number = models.IntegerField(max_length=5, verbose_name='Victim Number')
    is_approved = models.BooleanField(verbose_name='Is Approve')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    assistance_type = models.ForeignKey(AssistanceType, on_delete=models.CASCADE)
    assistance_given_date = models.DateField(verbose_name='Assistance Given Date', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Updated at')

    def __str__(self):
        return self.name










