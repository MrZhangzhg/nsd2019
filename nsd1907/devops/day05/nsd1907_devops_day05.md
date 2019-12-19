# nsd1907_devops_day05

## jenkins

- 实现CI功能

```mermaid
graph LR
d(程序员)--推送-->g(gitlab)
j(jenkins)--拉取-->g
a1(应用服务器)--拉取-->j
a2(应用服务器)--拉取-->j
a3(应用服务器)--拉取-->j
```

## 安装jenkins

- 配置一台虚拟机，它要能与gitlab服务器通信。并且它可以访问互联网
- 在虚拟机上安装jenkins

```shell
[root@node6 ~]# rpm -ivh jenkins-2.190.1-1.1.noarch.rpm 
[root@node6 ~]# systemctl start jenkins
[root@node6 ~]# systemctl enable jenkins
```

访问http://x.x.x.x:8080 -> 根据提示解锁 -> 自定义部分，点击
“选择插件来安装”，再选“无”后安装 -> 创建第一个管理员，选右>下角“使用admin继续登陆“ -> 保存并完成 -> 开始使用

### 修改管理员密码

页面右上角admin -> configure -> password -> Save

### 安装插件

#### 改为国内镜像站点安装插件

首页 -> Manage Jenkins -> Manage Plugins -> Advanced -> Update Site: https://mirrors.tuna.tsinghua.edu.cn/jenkins/ -> Submit

#### 安装插件

Available -> 按ctrl + f搜索 -> 选中Localization: Chinese (Simplified)和Git Parameter -> Install without restart -> 勾>选Restart Jenkins when installation is complete and no jobs are running



