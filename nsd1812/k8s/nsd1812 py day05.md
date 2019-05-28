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















