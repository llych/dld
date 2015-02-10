#!coding:UTF-8
#from celery import task
#import time
#@task()
#def add(x, y):
#    time.sleep(10)
#    return x + y


from celery.task import Task
from celery.registry import tasks
from devops.settings import ANSIBLE_TEMP
from ansible_app.models import *

#import ansible.runner

import subprocess,os

#class Ansible_Run(Task):
#    def run(self,pattern='*',forks=1,cmd=''):
#        msg=[]
#        results = ansible.runner.Runner(
#            pattern=pattern, forks=forks,
#            module_name='shell', module_args=cmd,
#        ).run()
#        if results is None:
#            return 'No hosts found'
            
#            #print "UP ***********"
#        for (hostname, result) in results['contacted'].items():
#            if not 'failed' in result:
#                msg.append("UP -- %s >>> %s" % (hostname, result['stdout']))

#        #print "FAILED *******"
#        for (hostname, result) in results['contacted'].items():
#            if 'failed' in result:
#                 msg.append( "FAILED -- %s >>> %s" % (hostname, result['msg']))

#        #print "DOWN *********"
#        for (hostname, result) in results['dark'].items():
#            msg.append("DOWN -- %s >>> %s" % (hostname, result))

#        return '\n'.join(msg)

#class RequestCindexTask(Task):

#    def run(self, key, field='user', **kwargs):

#        if field == 'user':
#            r = requests.get("http://127.0.0.1:8000/user/search?key=%s"%key)
#            return r.text
#        elif field == 'title':
#            pass
class Ansible_Run(Task):
    def run(self,hosts=[],cmd=''):
        
        try:
     

            resultsFile=os.path.join(ANSIBLE_TEMP,str(self.request.id)+'.out').replace('\\','/')
            hostFile=os.path.join(ANSIBLE_TEMP,str(self.request.id)+'.hosts').replace('\\','/')
            f=open(hostFile,'w')
            for ip in hosts:
                f.write(ip+'\n')
            f.close()
            result=open(resultsFile,'w')
            #cmd='ansible -i "{host}" all -m shell -f 100 -a "{cmd}"'.format(host=hostFile,cmd=cmd)
            cmd='{cmd} -i "{host}"'.format(host=hostFile,cmd=cmd)
            print cmd
            p=subprocess.Popen(cmd, shell=True, universal_newlines=True, stdin=subprocess.PIPE,stdout=result, stderr=result)
            p.wait()
            result.close()
            t=AnsibleTask.objects.get(task_id=self.request.id)
           
            t.status='完成'
            t.save()
        except Exception, e:
            t=AnsibleTask.objects.get(task_id=self.request.id)
           
            t.status='错误'
            t.save()

        return "OK"
        
tasks.register(Ansible_Run)