# nsd1905_review_day03

项目原则：符合生产环境，而不是包含了非常多的技术点。

架构、技术由业务驱动。

《大型网站技术架构》作者：阿里架构师李智慧

去IOE：IBM ／ ORACLE ／ EMC

![1569410423219](/root/.config/Typora/typora-user-images/1569410423219.png)

CDN：内容分发网络。它本质上就是一个大缓存，目标是让用户总是访问离他最近的缓存节点。

RAID：级别、构成、性能、容错、利用率

RAID0：2块以上，条带卷，性能最好，无容错，100％

RAID1(E)：镜像卷，2块以上，性能无提升，容错级别最高，50%

RAID5：3块以上，相当于是RAID0和RAID1的折中，(n-1)/n

RAID6：4块以上，提供两块盘作校验。

RAID10：RAID1＋RAID0



集群分类：

- 高可用集群HA
- 负载均衡集群LB
- 高性能计算集群HPC

LVS工作模式：

- DR
- NAT
- TUN

LVS调度算法：

- rr
- wrr
- lc
- wlc
- lblc
- lblc-r
- sh
- dh
- sed
- nq

keepalived双主模式：

- 分两组
- 每组有一个VIP
- 两台服务器在两个组中互为主从

web虚拟主机实现方式：

- 基于IP
- 基于端口
- 基于域名





