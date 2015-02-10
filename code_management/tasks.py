#!coding:UTF-8



from celery.task import Task
from celery.registry import tasks
from devops.settings import ANSIBLE_TEMP
from code_management.models import *

#import ansible.runner

import subprocess,os
#/root/.subversion/servers”中设置选项“store-plaintext-passwords”为“yes”或“no”，

class AddProject_Run(Task):
    def run(self,svn_path='',git_path='',svn_user='',svn_password=''):
        
        try:
     

            resultsFile=os.path.join(ANSIBLE_TEMP,str(self.request.id)+'.out').replace('\\','/')
            result=open(resultsFile,'w')
            if not os.path.exists(git_path):
                os.mkdir(git_path)
            cmd='svn checkout {svn_path} --username {svn_user} --password {svn_password} {git_path}'.format(svn_path=svn_path,svn_user=svn_user,svn_password=svn_password,git_path=git_path)
            print cmd
            p=subprocess.Popen(cmd, shell=True, universal_newlines=True, stdin=subprocess.PIPE,stdout=result, stderr=result)
            p.wait()

            result.close()
            #t=AnsibleTask.objects.get(task_id=self.request.id)
           
           # t.status='完成'
           # t.save()
        except Exception, e:
            #t=AnsibleTask.objects.get(task_id=self.request.id)
           
            #t.status='错误'
            #t.save()
            print e

        return "OK"
        
tasks.register(AddProject_Run)