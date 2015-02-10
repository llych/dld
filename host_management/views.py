#!coding:UTF-8
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect  
from host_management.models import *
from collections import OrderedDict
import json

def results(status="success",info=""):
    return json.dumps({"results":status,"info":info})


@login_required(login_url="/login")
def HostManagement(request):
    group=Group.objects.all()
    return render_to_response('host_management.html',{'user':request.user,'groups':group},context_instance=RequestContext(request))

def AddHost(request):
   
    if request.method == 'POST':
        try:
            errors=[]
        
            ip=request.POST.get('ip','')
            user=request.POST.get('user','')
            password=request.POST.get('password','')
            describe=request.POST.get('describe','')
            name=request.POST.get('name','')
            group=[str(g).replace('group_','') for g in request.POST if 'group_' in g]
            #print ip,user,password,describe
            #print group,'ggggggggggggg---'
            #for i in request.POST:
            #    print i,request.POST.get(i)
            if not ip:
                errors.append('ip 不能为空')
            if not user:
                errors.append('user 不能为空')
            if not group:
                errors.append('group 至少选择一个')
            if not errors:
                h=Host()
                h.ip=ip
                h.user=user
                h.password=password
                h.describe=describe
                h.name=name
                h.save()
                for g in group:
                    ag=Group.objects.get(name=g)
                    
                    h.group.add(ag)
                h.save()
            else:
                return HttpResponse(results('error','<br/>'.join(errors)))
        except Exception, e:
             
            return HttpResponse(results('error',str(e)))
    
        return HttpResponse(results('success'))
    return HttpResponse(results('error'))

def GetHost(request):
    res=[]
    
    hosts=Host.objects.all()
    if hosts:
        for h in hosts:
            d=OrderedDict()
            d["ip"]=h.ip
            d["user"]=h.user
            d["group"]=",".join([i.name for i in h.group.filter()])
            d["describe"]=h.describe
            d["created"]=h.created.strftime("%Y-%m-%d %H:%M:%S")
            #print d
            res.append(d)
        
        return HttpResponse(json.dumps(res))
    else:
        HttpResponse("None")

def DelHost(request):
    if request.method == 'POST':
        try:
            
            hosts=request.POST.getlist('hosts[]','')
            
            for host in hosts:
                h=Host.objects.get(ip=host)
                h.delete()
            return HttpResponse(results('success'))
        except Exception, e:
            return HttpResponse(results('error',str(e)))
    return HttpResponse(results('error'))

def UpHost(request):
   
    if request.method == 'POST':
        try:
            errors=[]
            
            ip=request.POST.get('ip','')
            user=request.POST.get('user','')
            password=request.POST.get('password','')
            describe=request.POST.get('describe','')
            name=request.POST.get('name','')
            group=[str(g).replace('group_','') for g in request.POST if 'group_' in g]
            #print ip,user,password,describe
            #print group,'ggggggggggggg---'
            #for i in request.POST:
            #    print i,request.POST.get(i)
            if not ip:
                errors.append('ip 不能为空')
            if not user:
                errors.append('user 不能为空')
            if not group:
                errors.append('group 至少选择一个')
            if not errors:
               
                h=Host.objects.get(ip=ip)
                print h
               
                h.user=user
                if password != '':
                    h.password=password
                h.describe=describe
                h.name=name
                h.save()
                for g in group:
                    ag=Group.objects.get(name=g)
                    
                    h.group.add(ag)
                h.save()
            else:
                return HttpResponse(f%('error','<br/>'.join(errors)))
        except Exception, e:
             
            return HttpResponse(results('error',str(e)))
    
        return HttpResponse(results('success'))
    return HttpResponse(results('error'))