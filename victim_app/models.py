from django.db import models
from assistance_app.models import Assistance


class Address(models.Model):
    id = models.IntegerField(max_length=10, verbose_name='ID', primary_key=True)
    address1 = models.CharField(max_length=255, verbose_name='Address1')
    address2 = models.CharField(max_length=255, verbose_name='Address2')
    city = models.CharField(max_length=255, verbose_name='City')
    mukim = models.CharField(max_length=255, verbose_name='Mukim')
    parlimen = models.CharField(max_length=255, verbose_name='Parlimen')
    state = models.CharField(max_length=255, verbose_name='State')
    poskod = models.IntegerField(max_length=5, verbose_name='Poskod')


class Profile(models.Model):
    ic = models.IntegerField(max_length=12, verbose_name='IC', primary_key=True)
    user_id = models.ForeignKey(Assistance, on_delete=models.CASCADE, verbose_name='User ID')
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE, verbose_name='Address ID')
    is_kir = models.BooleanField(default=True, verbose_name='Ketua Isi Rumah')
    salary = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Salary')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')


