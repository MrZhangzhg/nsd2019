# nsd1902_devops_day05

使用git时，如果不希望把某些文件、目录保存到版本库，可以在项目目录下创建一个名为.gitignore的文件，再把需要忽略的文件写进去。

```shell
[root@node5 pro2]# vim .gitignore
*.doc
*.docx
```

## jenkins

它是当前最流行的一款持续集成（CI）工具。

自动化运维平台：docker / ansible / jenkins / git

### 准备一台虚拟机，安装jenkins

- jenkins是java程序写的，所以要安装java
- 虚拟机需要能够访问互联网
- 虚拟机需要能够访问gitlab

### 安装jenkins

- 安装软件包，并启服务

```shell
[root@node7 ~]# yum install -y jenkins-2.177-1.1.noarch.rpm 
[root@node7 ~]# systemctl start jenkins
[root@node7 ~]# systemctl enable jenkins
```

- 访问jenkins的8080端口

- 注意，在安装插件页面，选择“选择插件来安装”，然后点击“无”。因为此时安装插件将会访问国外站点安装，速度慢。将来改成国内镜像站点安装。
- “创建第一个管理员用户”页面，点击右下角的“使用admin”
- 进入页面后，先点击右上角的“admin”三角号的下接菜单选configure。在此页面改密码。

### 安装插件

- 在首页上点击manage jenkins -> manage plugins -> advanced -> update site中的url填写：https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/current/update-center.json -> submit
- 点击Available选项卡，搜索找到[Localization: Chinese (Simplified)，勾选左侧的复选框，该插件用于中文支持。
- 点击Install without restart
- 勾选Restart jenkins... ... 
- 安装git parameter插件。用于访问git。









