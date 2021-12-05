from django.db import models
from auth_app.models import CustomUser


class AssistanceType(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Updated at')
    
    def __str__(self):
        return self.name


class Assistance(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name', null=True, blank=True)
    ic = models.CharField(max_length=255, verbose_name='Ic', default="")
    remark = models.TextField(verbose_name='Remark', null=True, blank=True)
    progress_percentage = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='Progress Percentage', null=True, blank=True)
    victim_number = models.IntegerField(verbose_name='Victim Number')
    is_approved = models.BooleanField(verbose_name='Is Approved', default=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    assistance_type = models.ForeignKey(AssistanceType, on_delete=models.CASCADE)
    assistance_given_date = models.DateField(verbose_name='Assistance Given Date', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Updated at')

    def __str__(self):
        return self.user.username + "-" + self.assistance_type.name










