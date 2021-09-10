from django.db import models
from simple_history.models import HistoricalRecords
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.hashers import check_password
import datetime
from authentication.models import Users

class FirmDetails(models.Model):
    firmname = models.CharField(max_length=100,unique=True,null=True,blank=False)
    nnid = models.CharField(max_length=25,unique=True,null=True,blank=False)
    email = models.EmailField(max_length=50,unique=True,null=True,blank=False)
    website = models.CharField(max_length=50,blank=True,null=True,unique=True)
    address = models.TextField(blank=False,null=True)
    city = models.CharField(max_length=50,unique=False,null=True,blank=False)
    country = models.CharField(max_length=50,unique=False,null=True,blank=False)
    zipcode = models.CharField(max_length=10,unique=False,null=True,blank=False)
    officephone = models.BigIntegerField(null=True,blank=False,unique=True)
    mobile = models.BigIntegerField(null=True,blank=False,unique=True)
    est_year = models.IntegerField(null=True,blank=False,unique=False)
    register_on = models.DateTimeField(auto_now_add=True,null=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Firm Details"

    def __str__(self):
        return str(self.firmname)

    @property
    def is_authenticated(self):
        return True

    def validate_password(self, password):
        return check_password(password,self.password)

class FirmStatus(models.Model):
    ACCOUNT_STATUS_CHOICES = (
    ('0','Invitation Send'),
    ('1','Approved'),
    ('2','Pending Approval'),
    ('3','Pendind Review'),
    ('4','Rejected'),
    ('5','Terminated')
    )

    firmname = models.ForeignKey(FirmDetails, on_delete=models.CASCADE,null=True,related_name='%(class)s_firm_name')
    status = models.CharField(max_length=50,choices=ACCOUNT_STATUS_CHOICES,null=True,blank=False,default=2)
    updated_on = models.DateField(auto_now_add=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = 'Firm Status'

    def __str__(self):
        return str(self.firmname)

@receiver(post_save,sender=FirmDetails)
def generate_user_status(sender,instance=None,created=False,**kwargs):
    if created:
        FirmStatus.objects.create(firmname=instance,updated_on=datetime.date.today())


class FirmsList(models.Model):
    firmname = models.ForeignKey(Users,on_delete=models.CASCADE, null=True,blank=False)

    def __str__(self):
        return str(self.firmname)


@receiver(post_save,sender=Users)
def generate_firms(sender,instance=None,created=True,**kwargs):
    objection_list = ['firm_client','admin','vendor']
    if created:
        if str(instance.user_type) in objection_list:
            pass
        else:
            FirmsList.objects.create(firmname=instance)