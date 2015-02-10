from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Group(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Host(models.Model):
    ip=models.CharField(max_length=30,unique=True)
    user=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    group=models.ManyToManyField(Group)
    describe=models.TextField(blank=True, null=True)
    name=models.CharField(max_length=30,blank=True, null=True)
    created  = models.DateTimeField(auto_now_add=True,verbose_name=_('created'))
    modified = models.DateTimeField(auto_now=True,verbose_name=_('modified'))
    def __str__(self):
        return self.ip
