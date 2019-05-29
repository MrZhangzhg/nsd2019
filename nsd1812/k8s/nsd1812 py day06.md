# nsd1812 py day06

## k8s

### 环境准备

- node1.tedu.cn  192.168.4.1/24，必须配网关，如果没有配置网关k8s无法启动。
- 将安装包拷贝到node1

### 安装

```shell
[root@node1 ~]# cd k8s_pkgs/
[root@node1 k8s_pkgs]# yum remove -y python-rhsm
[root@node1 k8s_pkgs]# yum install -y *
```

### 配置

```shell
[root@node1 k8s_pkgs]# vim /etc/sysconfig/docker
OPTIONS='--selinux-enabled=False --log-driver=journald --signature-verification=false'
[root@node1 k8s_pkgs]# vim /etc/docker/daemon.json 
{
  "insecure-registries" : ["192.168.4.254:5000"]
}
[root@node1 k8s_pkgs]# vim /etc/kubernetes/apiserver
把ServiceAccount从--admission-control删掉
[root@node1 k8s_pkgs]# vim /etc/kubernetes/kubelet 
KUBELET_POD_INFRA_CONTAINER="--pod-infra-container-image=192.168.4.254:5000/pod-infrastructure"
```

### 启服务

```shell
# master的组件
[root@node1 k8s_pkgs]# systemctl start etcd
[root@node1 k8s_pkgs]# systemctl enable etcd
[root@node1 k8s_pkgs]# systemctl start kube-apiserver
[root@node1 k8s_pkgs]# systemctl enable kube-apiserver
[root@node1 k8s_pkgs]# systemctl start kube-controller-manager
[root@node1 k8s_pkgs]# systemctl enable kube-controller-manager
[root@node1 k8s_pkgs]# systemctl start kube-scheduler
[root@node1 k8s_pkgs]# systemctl enable kube-scheduler
# node的组件
[root@node1 k8s_pkgs]# systemctl start docker
[root@node1 k8s_pkgs]# systemctl enable docker
[root@node1 k8s_pkgs]# systemctl start kubelet
[root@node1 k8s_pkgs]# systemctl enable kubelet
[root@node1 k8s_pkgs]# systemctl start kube-proxy
[root@node1 k8s_pkgs]# systemctl enable kube-proxy

```









