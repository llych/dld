from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class CodeProject(models.Model):
    project_name=models.CharField(max_length=50,unique=True)
    svn_path=models.CharField(max_length=200)
    git_path=models.CharField(max_length=200)
    remote_path=models.CharField(max_length=200)
    svn_user=models.CharField(max_length=100)
    svn_password=models.CharField(max_length=100)
    status=models.CharField(max_length=20)

    created  = models.DateTimeField(auto_now_add=True,verbose_name=_('created'))
    modified = models.DateTimeField(auto_now=True,verbose_name=_('modified'))
    def __str__(self):
        return self.project_name