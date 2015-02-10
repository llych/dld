# dld
上线回滚,批量部署
-----------------------------------  
    花了2周时间看 django book
    1周时间看 ansible
    几天的时候看 celery
    1周时间看 w3cschool 的js 基础
    勉强把功能给实现了
    联系: llych#126.com

* celery 任务队列(所有任务都由这管理)
* 批量执行命令,部署(ansible -shell playbook)
* php 代码上线回滚管理(根据版本号,从svn版本库,提取出文件列表,同步至本地目录(git控制,回滚需要),再同步生产环境)

### 基本流程<br />  
 ![image](https://github.com/llych/dld/blob/master/screenshots/dld1.png)
 
### 登录<br />
![image](https://github.com/llych/dld/blob/master/screenshots/dld2.jpg)
