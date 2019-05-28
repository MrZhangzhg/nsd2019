# nsd1812 py day05

## 自动化运维

平台化（ansible / git / gitlab / docker / jenkins / elk）、自动化（工具/脚本）、容器化（docker / k8s）、虚拟化

面试：准备项目（认真准备，把所有细节考虑到）

## DOCKER

### docker和虚拟机的区别

- 更高效的资源利用。虚拟机是一个完备的系统，容器只是一个进程。
- 虚拟机启动慢，容器是秒级
- 一致的运行环境
- CI/CD

### 容器核心概念

- 镜像
- 容器
- 仓库

镜像采用的是AUFS，实现分层结构。镜像是只读的。创建新镜像时，底层内容不变，只是给镜像增加了一个新层次。

容器可以认为是镜像的一次执行，是可读写的镜像。容器只是操作系统上的一个进程，进程执行完毕将会退出。不要假定容器会一直存在，应该假设它随时会崩溃。容器一旦出现故障，不要犹豫，直接将它删除，再启动一个。

仓库是镜像仓库，也可以自己创建私有仓库。

#### 镜像

```shell
[root@room8pc16 k8s]# docker search nginx
选择镜像，最好找官方的、STAR多的

# 通过busybox镜像运行echo，本地没有镜像将会自动在网上的仓库下载
[root@room8pc16 k8s]# docker run busybox echo Hello World

[root@room8pc16 k8s]# docker run -it --name mycent1 -h mycent1 centos bash
# ctrl + p / ctrl + q 退出容器，又不导致容器结束
[root@room8pc16 k8s]# docker logs mycent1   # 日志
[root@room8pc16 k8s]# docker exec -it mycent1 bash  # 新启动Bash
[root@room8pc16 k8s]# docker attach mycent1  # 连接到当前容器进程，不启动新进程
```

生成新的镜像，可以通过commit指令将容器封装成镜像。但是这样做是不推荐的，因为它将产生太多的垃圾内容。

#### 通过Dockerfile定制镜像

一般来说，新建一个空目录，在这里创建名为dockerfile的文件进行镜像定制。

```shell
[root@room8pc16 k8s]# mkdir -p /tmp/docker/dfile1
[root@room8pc16 k8s]# cd /tmp/docker/dfile1
[root@room8pc16 dfile1]# vim dockerfile
FROM centos
RUN echo 'Hello World' > /tmp/hi.txt
[root@room8pc16 dfile1]# docker build -t mycent1 .  # 构建镜像
[root@room8pc16 dfile1]# docker history mycent1  # 查看详情
[root@room8pc16 dfile1]# docker run -it mycent1 bash  # 测试
[root@dfc6051dda08 /]# ls /tmp/hi.txt 
/tmp/hi.txt
[root@dfc6051dda08 /]# cat /tmp/hi.txt
Hello World
```

新建镜像，执行多个指令：

```shell
[root@room8pc16 dfile1]# cd ..
[root@room8pc16 docker]# mkdir dfile2
[root@room8pc16 docker]# cd dfile2
[root@room8pc16 dfile2]# vim dockerfile
FROM centos
RUN yum install -y net-tools
RUN echo 'hello world' > /tmp/hi.txt
RUN mkdir /tmp/demo
[root@room8pc16 dfile2]# docker build -t mycent2 .
[root@room8pc16 dfile2]# docker history mycent2
```

通过history观察到mycent2镜像增加了三个层次，因为每个RUN指令增加一个层次。制作镜像时，最好不要出现太多额外的层次，所以dockerfile最好改为以下样式：

```shell
[root@room8pc16 dfile2]# vim dockerfile 
FROM centos
RUN yum install -y net-tools \
    && echo 'hello world' > /tmp/hi.txt \
    && mkdir /tmp/demo
[root@room8pc16 dfile2]# docker build -t mycent3 .
[root@room8pc16 dfile2]# docker history mycent3
# 发现构建的新镜像只有一个层次
```

> 注意：在构建镜像时使用的‘.’并不是指当前目录的意思，而是构建上下文环境context。docker是C/S模型运行，在构建时，客户端会把构建当前目录的内容拷贝到context，然后通过context环境执行构建。构建好的镜像放到服务器的镜像库中。

### Dockerfile指令

- FROM：基于哪个镜像进行构建
- RUN：在构建过程中运行的指令
- COPY：将从构建上下文目录中 \<源路径\> 的文件/目录复制到新的一层的镜像
  内的\<目标路径\>位置
- CMD：用于指定默认的容器主进程的启动命令的。

```shell
[root@room8pc16 dfile3]# vim dockerfile 
FROM centos
CMD /bin/echo Hello World
[root@room8pc16 dfile3]# docker build -t mycent4 .
[root@room8pc16 dfile3]# docker run --rm mycent4
Hello World
[root@room8pc16 dfile3]# docker run --rm -it mycent4 bash
[root@324bc2a59213 /]# exit
```

- ENTRYPOINT：与CMD类似，只不过它允许docker命令将参数传给ENTRYPOINT的命令。

```shell
[root@room8pc16 docker]# mkdir dfile4
[root@room8pc16 docker]# cd dfile4
[root@room8pc16 dfile4]# vim dockerfile
FROM centos
CMD ["curl", "-s", "https://ip.cn"]
[root@room8pc16 dfile4]# docker build -t mycent5 .
[root@room8pc16 dfile4]# docker run  --rm mycent5 
[root@room8pc16 dfile4]# docker run  --rm mycent5 -s  # -s被当作命令，要求容器运行，但是-s并不是一个有效的命令
docker: Error response from daemon: oci runtime error: exec: "-s": executable file not found in $PATH.

[root@room8pc16 dfile4]# docker rmi mycent5
[root@room8pc16 dfile4]# vim dockerfile 
FROM centos
ENTRYPOINT ["curl", "-s", "http://ip.cn"]
[root@room8pc16 dfile4]# docker build -t mycent5 .
[root@room8pc16 dfile4]# docker run  --rm mycent5 
# 容器将运行curl -s http://ip.cn
[root@room8pc16 dfile4]# docker run  --rm mycent5 -i
# 容器将运和地curl -s http://ip.cn -i
```

- ENV：配置环境变量

```shell
[root@room8pc16 docker]# mkdir dfile5
[root@room8pc16 docker]# cd dfile5
[root@room8pc16 dfile5]# vim dockerfile
FROM centos
ENV NAME=admin PASSWORD=123456
[root@room8pc16 dfile5]# docker build -t mycent6 .
[root@room8pc16 dfile5]# docker run -it --rm mycent6 bash
[root@de0c422bd4bd /]# echo $NAME
admin
[root@de0c422bd4bd /]# echo $PASSWORD
123456
```

- VOLUME：用户忘记使用-v将数据目录挂到宿主机，将会自动创建一个匿名卷。

```shell
[root@room8pc16 dfile5]# mkdir ../dfile6
[root@room8pc16 dfile5]# cd ../dfile6
[root@room8pc16 dfile6]# vim dockerfile
FROM centos
VOLUME /data
[root@room8pc16 dfile6]# docker build -t mycent7 .
[root@room8pc16 dfile6]# docker run -ti --rm mycent7 bash
[root@a7e16ff52fd7 /]# cp /etc/hosts /data/
ls \ 
/var/lib/docker/volumes/56479f6801520632d38cae130241e1467f2ae554a10c792fa628ae8c44ac605a/_data/
hosts
```

- EXPOSE：声明端口仅仅是声明容器打算使用什么端口而已,并不会自动在宿主进行

  端口映射。

```shell
[root@room8pc16 dfile6]# mkdir ../dfile7
[root@room8pc16 dfile6]# cd ../dfile7
[root@room8pc16 dfile7]# vim dockerfile
FROM centos
EXPOSE 80
[root@room8pc16 dfile7]# docker build -t mycent8 .
[root@room8pc16 dfile7]# docker run -idt -P mycent8 bash
# 宿主机将随机选择一个端口与容器的80端口映射
```



制作基于centos的httpd镜像

```shell
[root@room8pc16 docker]# mkdir dfile9
[root@room8pc16 docker]# cd dfile9
[root@room8pc16 dfile9]# vim dockerfile
FROM centos
RUN rm -f /etc/yum.repos.d/*
COPY ./server.repo /etc/yum.repos.d/
RUN yum install -y httpd
VOLUME /var/www/html/
EXPOSE 80
ENTRYPOINT ["httpd", "-D", "FOREGROUND"]
[root@room8pc16 dfile9]# vim server.repo
[server]
name=server
baseurl=ftp://172.17.0.1/centos7.4
gpgcheck=0
[root@room8pc16 dfile9]# docker build -t cent_httpd .
[root@room8pc16 dfile9]# docker run -v /tmp/html:/var/www/html -p 9000:80 -d cent_httpd
[root@room8pc16 dfile9]# echo '<h1>docker html</h1>' > /tmp/html/index.html
[root@room8pc16 dfile9]# curl http://127.0.0.1:9000
<h1>docker html</h1>
[root@room8pc16 dfile9]# docker rm -f 6d75ee51c3a5b  # 强制删除容器
[root@room8pc16 dfile9]# curl http://127.0.0.1:9000
curl: (7) Failed connect to 127.0.0.1:9000; 拒绝连接
[root@room8pc16 dfile9]# docker run -v /tmp/html:/var/www/html -p 9000:80 -d cent_httpd   # 使用相同的命令再次启动一个容器
[root@room8pc16 dfile9]# curl http://127.0.0.1:9000
<h1>docker html</h1>
```





















