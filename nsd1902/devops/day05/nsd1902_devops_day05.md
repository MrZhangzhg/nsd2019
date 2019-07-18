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











