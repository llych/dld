#!coding:UTF-8
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect  
from ansible_app.models import *

from django.core.paginator import Paginator, InvalidPage, EmptyPage

def LoginView(request):
    errors=[]
    if request.method == 'POST':
        print 'post'
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        #print username,password
        if not request.POST.get('username',''):
            errors.append('用户名为空')
        if not request.POST.get('password',''):
            errors.append('密码为空')
        if not errors:
            user = auth.authenticate(username=username,password=password)
            #print 'l---:',user
            
            if user is not None and user.is_active:
                auth.login(request,user)
                #return HttpResponse('You have logged in.')
                if 'next' in request.GET:
                    return HttpResponseRedirect(request.GET['next'])
                return HttpResponseRedirect('/')
            else:
                errors.append('用户 or 密码 错误')
    return render_to_response('user_login.html',\
                              {'errors':errors,}, \
                              context_instance=RequestContext(request))

def Logout(request):
    
    auth.logout(request)
    return HttpResponseRedirect("/")

#@login_required(login_url="/login",redirect_field_name='after')
@login_required(login_url="/login")
def Index(request):
    tasks_list=AnsibleTask.objects.all()
    paginator = Paginator(tasks_list, 5)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        tasks = paginator.page(page)
    except (EmptyPage, InvalidPage):
        tasks = paginator.page(paginator.num_pages)
    return render_to_response('index.html',{'user':request.user,'tasks':tasks},context_instance=RequestContext(request))


@login_required(login_url="/login")
def HostManagement(request):
   
    return render_to_response('hostmanagement.html',{'user':request.user},context_instance=RequestContext(request))
    