from django.db import models
from simple_history.models import HistoricalRecords
from django.dispatch import receiver
from django.db.models.signals import post_save
from authentication.models import Users

class FirmDetails(models.Model):
    ACCOUNT_STATUS_CHOICES = (
    ('0','Invitation Send'),
    ('1','Approved'),
    ('2','Pending Approval'),
    ('3','Pendind Review'),
    ('4','Rejected'),
    ('5','Terminated')
    )
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    firmname = models.CharField(max_length=100,unique=True,null=True,blank=True)
    nnid = models.CharField(max_length=25,unique=True,null=True,blank=True)
    email = models.EmailField(max_length=50,unique=True,null=True,blank=True)
    website = models.CharField(max_length=50,blank=True,null=True,unique=True)
    address = models.TextField(blank=True,null=True)
    city = models.CharField(max_length=50,unique=False,null=True,blank=True)
    country = models.CharField(max_length=50,unique=False,null=True,blank=True)
    zipcode = models.CharField(max_length=10,unique=False,null=True,blank=True)
    officephone = models.BigIntegerField(null=True,blank=True,unique=True)
    mobile = models.BigIntegerField(null=True,blank=True,unique=True)
    est_year = models.IntegerField(null=True,blank=True,unique=False)
    status = models.CharField(max_length=50,unique=False,null=True,blank=False,choices=ACCOUNT_STATUS_CHOICES,default="2")
    register_on = models.DateTimeField(auto_now_add=True,null=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Firm Details"

    def __str__(self):
        return str(self.firmname)


class FirmsList(models.Model):
    firmname = models.ForeignKey(Users,on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self):
        return str(self.firmname)


@receiver(post_save,sender=Users)
def generate_firms(sender,instance=None,created=True,**kwargs):
    if created and instance.user_type == 'firm':
        FirmsList.objects.create(firmname=instance)    
    else:
        pass
            