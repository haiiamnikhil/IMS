from django.db import models
from authentication.models import Users
from simple_history.models import HistoricalRecords
from django.db.models.signals import post_save
from django.dispatch import receiver
from firm_management.models import FirmDetails


class UserDesinations(models.Model):
    firmname = models.ForeignKey(FirmDetails, on_delete=models.SET_NULL, null=True, related_name='%(class)s_firmname')
    key = models.CharField(max_length=50, unique=False, null=True, blank=True)
    designation = models.CharField(max_length=50,unique=True, null=True, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{str(self.designation)}, {str(self.firmname)}"

    class Meta:
        verbose_name_plural = 'User Designations'
    
    def save( self, *args, **kwargs ):
        self.key = f"{self.designation.replace(' ', '_')}"
        super( UserDesinations, self ).save( *args, **kwargs )


class UserDetails(models.Model):
    ACCOUNT_STATUS_CHOICES = (
    ('0','Invitation Send'),
    ('1','Approved'),
    ('2','Pending Approval'),
    ('3','Pendind Review'),
    ('4','Rejected'),
    ('5','Terminated')
    )

    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True,blank=False,related_name='%(class)s_user')
    firmname = models.CharField(max_length=150,unique=False,null=True,blank=True)
    fullname = models.CharField(max_length=100,unique=False,null=True,blank=True)
    userid = models.CharField(max_length=25,unique=True,null=True,blank=True)
    email = models.EmailField(max_length=50,unique=True,null=True,blank=True)
    designation = models.ForeignKey(UserDesinations,on_delete=models.DO_NOTHING,null=True)
    address = models.TextField(blank=True,null=True)
    city = models.CharField(max_length=50,unique=False,null=True,blank=True)
    country = models.CharField(max_length=50,unique=False,null=True,blank=True)
    zipcode = models.CharField(max_length=10,unique=False,null=True,blank=True)
    mobile = models.BigIntegerField(null=True,blank=True,unique=True)
    join_date = models.DateField(auto_now_add=True,null=True)
    register_on = models.DateTimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length=50,unique=False,null=True,blank=False,choices=ACCOUNT_STATUS_CHOICES,default="2")
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "User Details"

    def __str__(self):
        return str(self.fullname)


@receiver(post_save,sender=Users)
def generate_user_details(sender,instance=None,created=False,**kwargs):
    if created and instance.user_type == 'firm':
        FirmDetails.objects.create(user=instance,firmname=instance.firmname,nnid=instance.nnid,email=instance.email)
    elif created and instance.user_type == 'firm_user':
        UserDetails.objects.create(user=instance,firmname=instance.user_firmname,
        fullname=instance.fullname,email=instance.email)
    else:pass


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


class UserOnboardingTracker(models.Model):
    ONBOARDING_LEVELS = (
        ('0','Get Started'),
        ('1','Done')
    )
    user = models.ForeignKey(Users,on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=50,unique=False,null=True,choices=ONBOARDING_LEVELS,default='0')
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
    
@receiver(post_save,sender=Users)
def generate_user_onboard_status(sender,instance=None,created=False,**kwargs):
    objection_list = ['firm','firm_user','vendor']
    if created and instance.user_type in objection_list:
        UserOnboardingTracker.objects.create(user=instance)