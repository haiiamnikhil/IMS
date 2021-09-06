from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords


class Users(AbstractUser):
    email = models.CharField(_('Email'), max_length=100,unique=True)
    history = HistoricalRecords()
