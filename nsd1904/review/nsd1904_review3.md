# nsd1904_review3

## 集群

- 高性能计算HPC
- 高可用HA：KeepAlived
- 负载均衡LB：HAProxy / Nginx / LVS / F5

### CEPH支持的存储类型

- 块存储
- 对象存储
- 文件系统

## keepalived双主

- 两台KeepAlived服务器互为主备
- 假设有web和邮件的负载均衡集群
- A调度器配置为web的主，邮件的从调度器
- B调度器配置为web的从，邮件的主调度器

## 代理

- 代理服务器：在局域网中提高对外网的访问速度
- 反向代理：在服务器一侧，提升对服务器的访问速度

## CDN

- 内容分发网络
- 本质上就是一个大缓存网络
- 目标是让用户总是访问离他/她最近的缓存节点

## KVM切换器/KVM交换机

- K: Keyboard键盘
- V: Video显示
- M: Mouse鼠标









