# nsd1903_review5

## CDN：内容分发网络

使得用户总是访问离他最近的缓存节点。

WWW: World Wide Web  ->  World Wide Wait。

DNS：域名系统

DNS名称是一棵倒置的树，树根是 [ . ] ，以下是一级域（也叫顶级域），然后是二级、三级……最多127级。

FQDN（完全限定域名）＝ 主机名.域名后缀



DNS的查询方式：递归查询、迭代查询



客户机解析名称时的顺序：

1. 本机缓存
2. 本机的hosts
3. 本地DNS服务器（配置网络参数时指定的DNS服务器）
4. 本地DNS将会发起向根服务器的迭代查询



DNS常用的资源记录类型：

- SOA：起始授权，权威服务器
- NS：名称服务器，所有的DNS服务器都对应NS记录
- A：将名称解析为IP地址
- PTR：反向记录，将IP地址解析为名称
- MX：邮件交换器
- CNAME：别名记录

```shell
[root@room8pc16 day03]# nslookup 
> set type=ns   # 查询163.com中所有的DNS服务器
> 163.com

> set type=soa   # 查询163.com中的权威服务器
> 163.com

> set type=a    # 查询www.163.com的IP地址
> www.163.com

```



正向代理：一般在用户端，为用户提升速度

反向代理：一般在服务器端，为服务器提供速度



web服务器：虚拟主机实现方式

虚拟主机：一台服务器上运行多个网站

- 基于IP地址
- 基于端口
- 基于域名



tomcat：主要用于发布java程序

java程序需要编译。一般来说，发布到tomcat的java程序，首先要编译成war包。将war包放到tomcat的网站目录下，重启tomcat进行自动发布。

war包的制作可以通过mvn实现。



ceph：是一种分布式文件系统。它是一种面向未来的存储。

- 块存储
- 文件系统
- 对象存储



ansible / git / docker / jenkins

与ansible类似的工具：puppet / saltstack

docker：容器

- 镜像
- 容器
- 仓库



zabbix监控





















