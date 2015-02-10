#!coding:UTF-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from host_management.models import *

from ansible_app.models import *
from ansible_app.tasks import *
from devops.settings import ANSIBLE_TEMP

import json
import os
import re


from celery.result import AsyncResult
# Create your views here.
import json
def results(status="success",info=""):
    return json.dumps({"results":status,"info":info})


@login_required(login_url="/login")
def Ansible_app(request):

    return render_to_response('ansible.html',{'user':request.user},context_instance=RequestContext(request))

#批量执行任务
@login_required(login_url="/login")
def AddTask(request):
    badcmd = ['reboot','rm','kill','pkill','shutdown','half','mv','dd','mkfs','>','wget','user','group']
    if request.method == 'POST':
        try:
            errors=[]
            ips=request.POST.getlist('ip[]','')
            module=request.POST.get('module','')
            cmd=request.POST.get('cmd','')
            if len(ips)==0:
                errors.append('没有选择主机')
            if not cmd:
                errors.append("没有输入命令|模块ID")
            else:
                for i in badcmd:
                    if i in cmd:
                        errors.append(str(cmd)+' 不允许执行')
            
            if module == "ansible-shell":
                cmds='ansible all -m shell -f 100 -a "{cmd}"'.format(cmd=cmd)
                
            else:
                try:
                    t=TasksModule.objects.get(id=cmd)
                    cmds = 'ansible-playbook {playbook}'.format(playbook=t.playbook)
                    cmd = 'ID:'+cmd+' '+t.name
                except Exception, e:
                    errors.append('ansible 模块ID:'+str(cmd)+' 不存在')
                
            if not errors:
                r = Ansible_Run.delay(hosts=ips,cmd=cmds)
                t=AnsibleTask()
                t.task_id=r.task_id
                t.status='新增'
                t.info=cmd
                t.save()
                #print t
                for ip in ips:
                    hobj=Host.objects.get(ip=ip)
                    t.host.add(hobj)
                t.save()
                return HttpResponse(results('success'))
            
            return HttpResponse(results('error','|'.join(errors)))
        except Exception, e:
            return HttpResponse(results('error',str(e)))
    return HttpResponse(results('error'))

#返回任务完成数据页
def GetTask(request,taskID):
    resultsFile=os.path.join(ANSIBLE_TEMP,taskID+'.out').replace('\\','/')
    results=[]
    if os.path.isfile(resultsFile):

        
        for line in open(resultsFile).readlines():
            #if "FAILED" in line or 'failed' in line or 'FATAL' in line:
            if re.search('FAILED|failed|FATAL',line):
                line='<b><font color="red" size="4">'+line+'</font>'
            elif "rc=" in line:
                line='<b><font color="blue" size="4">'+line+'</font>'
            results.append(line)
        #print results
        results='<br/>'.join(results)
        return HttpResponse(results)
    else:
        return HttpResponse('暂无数据')

#ajax 获取任务状态
def GetTaskStatus(request):
    if request.method == 'POST':
        #try:
        errors=[]
        info=[]
        tasks=request.POST.getlist('tasks[]','')
        if len(tasks)==0:
            return HttpResponse(results('error'))
        else:
            for task in tasks:
                ansible_celery=AsyncResult(task)
                status=ansible_celery.status
                #print task,status
                if status == 'FAILURE':
                    #task_status=AnsibleTask.objects.get(task_id=task)
                    #task_status.status='失败'
                    #task_status.save()
                    info.append({task:'错误'})
                elif status == 'STARTED':
                    #task_status=AnsibleTask.objects.get(task_id=task)
                    #task_status.status='执行中'
                    #task_status.save()

                    info.append({task:'执行中'})
                elif status == 'SUCCESS':
                    #task_status=AnsibleTask.objects.get(task_id=task)
                    #task_status.status='完成'
                    #task_status.save()
                    info.append({task:'完成'})
                else:
                    t=AnsibleTask.objects.filter(task_id=task)
                    if len(t)==0:
                        info.append({task:'已删除'})
                    else:
                        info.append({task:t[0].status})
            return HttpResponse(results('success',info))
        
        
        #except Exception, e:
        #    return HttpResponse(results('error',str(e)))
    return HttpResponse(results('error'))


#返回json| ansbile 任务模块
def GetAnsbileModule(request):
    res=[]
    
    task_module=TasksModule.objects.all()
    if task_module:
        for t in task_module:
            d={}
            d["id"]=t.id
            d["name"]=t.name
            
            d["playbook"]=t.playbook
            d["created"]=t.created.strftime("%Y-%m-%d %H:%M:%S")
            #print d
            res.append(d)
        
        return HttpResponse(json.dumps(res))
    else:
        HttpResponse("None")

#增加 ansible playbook 任务模块
def AddAnsbileModule(request):
   
    if request.method == 'POST':
        try:
            errors=[]
        
            name=request.POST.get('name','')
            playbook=request.POST.get('playbook','')

           
            #print ip,user,password,describe
            #print group,'ggggggggggggg---'
            #for i in request.POST:
            #    print i,request.POST.get(i)
            if not name:
                errors.append('name 不能为空')
            if not playbook:
                errors.append('playbook 不能为空')
            elif not os.path.isfile(playbook):
                errors.append(str(playbook)+' 文件不存在')
            if not errors:
                m=TasksModule()
                m.name=name
                m.playbook=playbook
                m.save()
               
            else:
                return HttpResponse(results('error','<br/>'.join(errors)))
        except Exception, e:
             
            return HttpResponse(results('error',str(e)))
    
        return HttpResponse(results('success'))
    return HttpResponse(results('error'))

#删除模块
def DelAnsbileModule(request):
    if request.method == 'POST':
        try:
            
            ids=request.POST.getlist('ids[]','')
            
            for i in ids:
                print i
                m=TasksModule.objects.get(id=i)
                #print m
                m.delete()
            return HttpResponse(results('success'))
        except Exception, e:
            return HttpResponse(results('error',str(e)))
    return HttpResponse(results('error'))


#更新模块
def UpAnsbileModule(request):
   
    if request.method == 'POST':
        try:
            errors=[]
            id=request.POST.get('id','')
            name=request.POST.get('name','')
            playbook=request.POST.get('playbook','')

           
            #print ip,user,password,describe
            #print group,'ggggggggggggg---'
            #for i in request.POST:
            #    print i,request.POST.get(i)
            if not id:
                errors.append('获取任务id 出错')
            if not name:
                errors.append('name 不能为空')
            if not playbook:
                errors.append('playbook 不能为空')
            elif not os.path.isfile(playbook):
                errors.append(str(playbook)+' 文件不存在')
 
            if not errors:
                m=TasksModule.objects.get(id=id)
                m.name=name
                m.playbook=playbook
                m.save()
               
            else:
                return HttpResponse(results('error','<br/>'.join(errors)))
        except Exception, e:
             
            return HttpResponse(results('error',str(e)))
    
        return HttpResponse(results('success'))
    return HttpResponse(results('error'))