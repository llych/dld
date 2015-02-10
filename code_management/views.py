#!coding:UTF-8
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect  
from code_management.models import *

from code_management.tasks import *

# Create your views here.

import json
def results(status="success",info=""):
    return json.dumps({"results":status,"info":info})


@login_required(login_url="/login")
def CodeIndex(request):
    p=CodeProject.objects.all()
    return render_to_response('code.html',{'user':request.user,'projects':p},context_instance=RequestContext(request))

def AddProject(request):
    
    if request.method == 'POST':
        try:
            errors=[]
            
            project_name=request.POST.get('project_name','')
            svn_path=request.POST.get('svn_path','')
            git_path=request.POST.get('git_path','')
            remote_path=request.POST.get('remote_path','')
            svn_user=request.POST.get('svn_user','')
            svn_password=request.POST.get('svn_password','')

            if not project_name:
                errors.append("项目命称不能为空")
            if not svn_path:
                errors.append("svn 路径不能为空")
            if not git_path:
                errors.append("git 路径不能为空")
            if not remote_path:
                errors.append("远程路径不能为空")
            if not svn_user:
                errors.append("svn 用户需要指定")
            if not svn_password:
                errors.append("svn 密码需要指定")
    
            

            if not errors:
                
                p=CodeProject()
                p.project_name=project_name
                p.svn_path=svn_path
                p.git_path=git_path
                p.remote_path=remote_path
                p.save()
                t=AddProject_Run.delay(svn_path=svn_path,svn_user=svn_user,svn_password=svn_password,git_path=git_path)
                print t.task_id
                

                return HttpResponse(results('success'))
            
            return HttpResponse(results('error','|'.join(errors)))
        except Exception, e:
            return HttpResponse(results('error',str(e)))
    return HttpResponse(results('error'))

def DelProject(request):
    
    if request.method == 'POST':
        try:
            errors=[]
            
            projectid=request.POST.get('projectid','')


               
            p=CodeProject.objects.get(id=projectid)
            p.delete()

            return HttpResponse(results('success'))
            
            
        except Exception, e:
            return HttpResponse(results('error',str(e)))
    return HttpResponse(results('error'))