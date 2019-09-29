# nsd1908_network_day02

## VLAN：虚拟局域网

### 广播和广播域：

某一节点发送广播信息，能够被多大的范围接收就是一个广播域。

### VLAN作用

划分广播域，实现广播控制。它可以将大广播域划分成多个小的广播域，把广播控制在一个小的范围。

### 广播地址

IP：255.255.255.255  

MAC：FF:FF:FF:FF:FF:FF

## 配置VLAN

1. 查看VLAN。默认所有的接口都处于vlan1

```shell
[sw1]display vlan
```

2. 创建VLAN

```shell
# 创建1个VLAN，ID是2，名字是ops
[sw1]vlan 2
[sw1-vlan2]description ops
[sw1-vlan2]display this   # 查看当前模式下的配置
# 创建3个vlan，ID分别是3，5，7
[sw1]vlan batch 3 5 7
# 创建ID号从11到15的VLAN
[sw1]vlan batch 11 to 15
# 为vlan3改名
[sw1]vlan 3
[sw1-vlan3]description dev

# 删除vlan
[sw1]undo vlan 15
[sw1]undo vlan batch 5 7
[sw1]undo vlan batch 11 to 14
```

3. 将端口加入vlan
   - 端口模式分为接入和中继
   - 接入端口：仅能属于一个VLAN
   - 中继端口：不属于任何VLAN，但是可以承载所有VLAN的数据

```shell
# 将单个端口加入vlan
[sw1]int e0/0/1
[sw1-ethernet0/0/1]port link-type access
[sw1-ethernet0/0/1]port default vlan 2

# 将不连接的端口加入到vlan2，首先创建端口组，再对端口组进行配置
[sw1]port-group 1
[sw1-port-group-1]group-member e0/0/2 e0/0/5
[sw1-port-group-1]port link-type access
[sw1-port-group-1]port default vlan 2

# 将连续的端口加入到vlan3
[sw1]port-group 2
[sw1-port-group-1]group-member e0/0/3 to e0/0/4
[sw1-port-group-1]port link-type access
[sw1-port-group-1]port default vlan 3
```

## trunk中继

- 用在交换机之间，可以实现不同交换机上相同VLAN通信
- 中继链路不属于任何VLAN
- 中继链路可以承载所有VLAN的数据

```shell
[sw1]int g0/0/1
[sw1-gigabyte0/0/1]port default vlan 1   # 恢复为默认配置
[sw1-gigabyte0/0/1]port link-type trunk  # 修改端口类型为trunk
[sw1-gigabyte0/0/1]port trunk allow-pass vlan all # 允许所有vlan通过

[sw2]int g0/0/1
[sw2-gigabyte0/0/1]port default vlan 1   # 恢复为默认配置
[sw2-gigabyte0/0/1]port link-type trunk  # 修改端口类型为trunk
[sw2-gigabyte0/0/1]port trunk allow-pass vlan all # 允许所有vlan通过
```

> 附：关闭设备日志输出
>
> [sw1] undo info-center enable

## 链路聚合

- 也叫以太通道
- 如果交换机之间只有一条线路，这条链路可能成为网络的瓶颈
- 可以在交换机之间再增加额外的链路，使多条链路成为一个逻辑链路
- 参与链路聚合的端口需要有相同的状态，如链路类型、速率

```shell
[sw1]clear configuration g0/0/1  # 清除g0/0/1的自定义配置
[sw1]int Eth-trunk 1   # 创建eth-trunk1端口
[sw1-Eth-Trunk1]trunkport gigabyte 0/0/1 0/0/2
[sw1-Eth-Trunk1]port link-type trunk
[sw1-Eth-Trunk1]port trunk allow-pass vlan all

[sw2]clear configuration g0/0/1
[sw2]int Eth-trunk 1
[sw2-Eth-Trunk1]trunkport gigabyte 0/0/1 0/0/2
[sw2-Eth-Trunk1]port link-type trunk
[sw2-Eth-Trunk1]port trunk allow-pass vlan all
```

## 网络层

- 重要的协议是IP协议
- 重要的地址是IP地址
- 重要的设备是路由器。路由器的作用是转发数据包，决定数据包的路径，这叫作路由

### ICMP：Internet控制消息协议

* 工作在网络层，用于测试两个IP地址是否可以通信

### ARP：地址解析协议

- 用于将IP地址解析为MAC地址
- 工作方式是广播

```shell
[root@room8pc16 network]# arp -n   # 显示本机的arp缓存
```

## 三层交换

- 三层交换机，既具有二层交换功能，又具有三层路由功能
- 配置三层交换机，只要把vlan当成端口，配置IP地址即可
- VLAN端口物理上不存在，所以叫作交换虚拟端口，SVI

### 基础配置

![1569573414007](/root/.config/Typora/typora-user-images/1569573414007.png)

- 在所有的交换机上创建vlan2/vlan3

```shell
[Huawei]vlan batch 2 3
```

- 在LSW1上，pc1/2加入vlan2；pc3/4加入vlan3

```
[sw1]port-group 1
[sw1-port-group-1]group-member e0/0/1 e0/0/2
[sw1-port-group-1]port link-type access
[sw1-port-group-1]port default vlan 2
[sw1]port-group 2
[sw1-port-group-2]group-member e0/0/3 e0/0/4
[sw1-port-group-2]port link-type access
[sw1-port-group-2]port default vlan 3
```

- 在所有交换机之间创建中继链路

```shell
[sw1]int g0/0/1
[sw1-gigabyte0/0/1]port link-type trunk
[sw1-gigabyte0/0/1]port trunk allow-pass vlan all
```

- 三层交换机配置三层交换
- 每个VLAN必须是不同网络
- vlan端口的IP地址是该vlan的网关
  - PC1: 192.168.1.10 / 255.255.255.0 / 192.168.1.1
  - PC2: 192.168.1.20 / 255.255.255.0 / 192.168.1.1
  - PC3: 192.168.3.30 / 255.255.255.0 / 192.168.3.1
  - PC4: 192.168.3.40 / 255.255.255.0 / 192.168.3.1

```shell
[ms1]int vlanif 2
[ms1-Vlanif2]ip address 192.168.1.1 24  # 24表示网络位有24位
[ms1]int vlanif 3
[ms1-Vlanif3]ip address 192.168.3.1 24
```

- 网络通信时，发送端判断自己与目标是不是同一网络，如果是则直接发送，如果不是则发送给网关

## 路由

- 路由，就是选择路径
- 选择路由的方式有静态和动态之分。静态是管理员手工配置的，动态路由是通过路由协议自动学习来的

### 路由器工作原理

- 路由器根据路由表做出数据包的转发决定
- 路由表中存储的是最佳路径，而不是全部路径
- 路由器如果发现目标地址未知，则丢弃数据包

![1569576623813](/root/.config/Typora/typora-user-images/1569576623813.png)

pc1: 192.168.1.10 / 255.255.255.0 / 192.168.1.1

pc2: 192.168.3.20 / 255.255.255.0 / 192.168.3.1

AR1: g0/0/0  192.168.1.1 / 255.255.255.0

AR1: g0/0/1 192.168.2.1 / 255.255.255.0

AR2: g0/0/0 192.168.3.1 255.255.255.0

AR2: g0/0/1 192.168.2.2 255.255.255.0

### 路由表的形成

- 路由器端口配置上IP地址，就会出现到该网络的直连路由
- 管理员手工配置静态、缺省路由
- 管理员还可以配置路由协议，路由器自动学习路由

```shell
[R1]int g0/0/0
[R1-gigabyte0/0/0]ip address 192.168.1.1 24
[R1]int g0/0/1
[R1-gigabyte0/0/1]ip address 192.168.2.1 24
[R1]display ip routing-table   # 查看路由表
# 静态路由 ip route-static 目标网络 掩码长度 下一跳的地址
[R1]ip route-static 192.168.3.0 24 192.168.2.2

[R2]int g0/0/0
[R2-gigabyte0/0/0]ip address 192.168.3.1 24
[R2]int g0/0/1
[R2-gigabyte0/0/1]ip address 192.168.2.2 24
[R2]display ip routing-table   # 查看路由表
# 静态路由 ip route-static 目标网络 掩码长度 下一跳的地址
[R2]ip route-static 192.168.1.0 24 192.168.2.1

[R1]display ip routing-table
[R2]display ip routing-table

```





