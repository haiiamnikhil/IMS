from django.db import models
from authentication.models import Users
from simple_history.models import HistoricalRecords
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

class UserInvites(models.Model):
    email = models.EmailField(max_length=100,unique=True,null=True,blank=False)
    first_name = models.CharField(max_length=50, null=True, blank=False)
    last_name = models.CharField(max_length=50, unique=False,null=True,blank=False)
    firm_name = models.ForeignKey(Users, on_delete=models.CASCADE,null=True,related_name='%(class)s_firm_name')
    invite_url = models.URLField(max_length=400,unique=True,blank=False)
    referred_by = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, related_name='%(class)s_refered_by')
    approved_by = models.ForeignKey(Users, on_delete=models.DO_NOTHING,null=True, related_name='%(class)s_approved_by')
    invite_send = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "User Invites"

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)


class UserStatus(models.Model):
    ACCOUNT_STATUS_CHOICES = (
    ('0','Invitation Send'),
    ('1','Approved'),
    ('2','Pending Approval'),
    ('3','Pendind Review'),
    ('4','Rejected'),
    ('5','Terminated')
    )
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, related_name='%(class)s_user')
    status = models.CharField(max_length=50,choices=ACCOUNT_STATUS_CHOICES,default=2,null=True,blank=False)
    updated_on = models.DateField(auto_now_add=False,default=datetime.date.today())
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "User Status"

    def __str__(self):
        return str(self.user)


@receiver(post_save,sender=Users)
def generate_user_status(sender,instance=None,created=False,**kwargs):
    if created:
        UserStatus.objects.create(user=instance,updated_on=datetime.date.today())