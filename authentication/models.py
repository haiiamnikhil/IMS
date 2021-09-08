from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords


class Users(AbstractUser):
    USER_TYPES = (
        ('firm','Firm'),
        ('admin','Admin'),
        ('firm_client','Firm Client'),
        ('vendor','Vendor')
    )
    nnid = models.BigIntegerField(null=True)
    email = models.CharField(_('Email'), max_length=100,unique=True)
    username = models.CharField(_('Username'), max_length=100,unique=True,blank=True,null=True)
    firmname = models.CharField(max_length=100,unique=True,blank=True,null=True)
    user_type = models.CharField(max_length=50,choices=USER_TYPES,null=True,blank=False)
    history = HistoricalRecords()

    def __str__(self):
        return str(self.username or self.firmname)