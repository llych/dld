from django.contrib import admin
from code_management.models import *
# Register your models here.

class CodeProjectAdmin(admin.ModelAdmin):
    list_display=('project_name','svn_path','git_path','remote_path','created')

admin.site.register(CodeProject,CodeProjectAdmin)