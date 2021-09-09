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
    nnid = models.BigIntegerField(null=True,blank=True,unique=True)
    email = models.CharField(_('Email'), max_length=100,unique=True)
    fullname = models.CharField(max_length=100,unique=False,null=True,blank=True)
    username = models.CharField(_('Username'), max_length=100,unique=True,blank=True,null=True)
    firmname = models.CharField(max_length=100,unique=True,blank=True,null=True)
    user_firmname = models.CharField(max_length=100,blank=True,null=True)
    user_type = models.CharField(max_length=50,choices=USER_TYPES,null=True,blank=False)
    history = HistoricalRecords()

    def __str__(self):
        return str(self.username or self.firmname or self.fullname)
    
    def save( self, *args, **kwargs ):
        self.fullname = f'{self.first_name} {self.last_name}'
        super( Users, self ).save( *args, **kwargs )