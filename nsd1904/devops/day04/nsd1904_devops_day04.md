# nsd1904_devops_day04

CI / CD：持续集成 / 持续交付

流行的自动化运维平台：docker / k8s / ansible / git / jenkins

准备三台机器

- node4.tedu.cn: 程序员PC
- node5.tedu.cn: gitlab服务器  -> 4GB以上内存
- node6.tedu.cn: jenkins

## git

- 软件版本管理系统
- 分布式

```shell
# 安装
[root@node4 ~]# yum install -y git
# 配置基础信息
[root@node4 ~]# git config --global user.name "zzg"
[root@node4 ~]# git config --global user.email "zzg@tedu.cn"
[root@node4 ~]# git config --global core.editor vim
# 查看
[root@node4 ~]# git config --list
[root@node4 ~]# cat ~/.gitconfig 

```















