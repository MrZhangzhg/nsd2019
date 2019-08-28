# nsd1907_net_day02

## 网络的通信类型

- 单播unicast：一对一
- 多播，也叫组播multicast：一对部分
- 广播broadcast：一对所有
- 在ipv6中，没有广播了，增加的是任播anycast。任播地址与单播地址一样，只不过这个地址配置在了多个节点上。

## 广播域

- 设备发出广播后，能够接收到广播的所有设备的集合是一个广播域。

- 没有任何配置的情况下，多台交换机连接起来，也是处于一个广播域。
- 交换机会将以下数据帧向所有端口发送
  - 广播
  - 组播
  - 未知地址的单播

## VLAN：虚拟局域网

- 最主要的作用是划分广播域，实现广播控制

### VLAN配置

- 创建VLAN：每个VLAN都有一个ID号，还可以添加可选的名字
- 将端口划分到VLAN

```shell
# 查看VLAN信息，默认所有端口都在vlan1中
<Huawei>system-view
[Huawei]display vlan  # 查看VLAN

# 创建一个VLAN
[Huawei]vlan 10    # VLAN id号范围是1-4094
[Huawei-vlan10]description ops   # VLAN10是运维部VLAN
[Huawei-vlan10]display this  # 查看当前模式下有哪些配置

# 批量创建VLAN
[Huawei]vlan batch 15 20   # 创建两个VLAN
[Huawei]vlan batch 21 to 25  # 创建5个VLAN
[Huawei]display vlan

# 删除VLAN：在创建VLAN的命令前加undo
[Huawei]undo vlan 20
[Huawei]undo vlan batch 15 21
[Huawei]undo vlan batch 22 to 25
```

端口类型

- 接入端口：接入端口仅属于一个VLAN
- 中继端口：不属于任何VLAN，但是可以承载所有VLAN的数据

```shell
[Huawei]int g0/0/1
[Huawei-GigabitEthernet0/0/1]port link-type access  # 设置端口类型
[Huawei-GigabitEthernet0/0/1]port default vlan 10   # 加入vlan10
[Huawei-GigabitEthernet0/0/1]display this

# 批量将端口加入VLAN
[Huawei]port-group 1   # 创建端口组，组号为1
[Huawei-port-group-1]group-member g0/0/5 g0/0/8  # 将不连续端口加入组
[Huawei-port-group-1]group-member g0/0/11 to g0/0/15 # 将连续端口加入组
[Huawei-port-group-1]port link-type access
[Huawei-port-group-1]port default vlan 10
[Huawei]display vlan
```

综合练习：

- 两台交换机sw1和sw2
- sw1:
  - vlan1: g0/0/1 - g0/0/2     pc1: 192.168.1.10  pc2: 192.168.1.20
  - vlan2: g0/0/3 - g0/0/4     pc3: 192.168.2.10  pc4: 192.168.2.20
  - vlan3: g0/0/5 - g0/0/6     pc5: 192.168.3.10  pc6: 192.168.3.20
  - g0/0/24 连接 sw2 g0/0/24
- sw2:
  - vlan1: g0/0/1 - g0/0/2     pc7: 192.168.1.70  pc8: 192.168.1.80
  - vlan2: g0/0/3 - g0/0/4     pc9: 192.168.2.90  pc10: 192.168.2.100
  - vlan3: g0/0/5 - g0/0/6     pc11: 192.168.3.110  pc12: 192.168.3.120
  - g0/0/24 连接 sw1 g0/0/24

### 设备网络参数

- IP地址：设备的地址
- 子网掩码：判断地址属于哪个网络
- 网关：数据包发出自己网络必须经过的地址

网络通信：A设备与B设备通，A先判断B与自己是不是在同一网络，如果是则直接发送；如果不是，则发往网关。

## Trunk中继

- 中继链路主要用在交换机之间
- 中继链路不属于任何VLAN，但是允许所有VLAN的数据通过

```shell
# 配置中继，两个步骤。注意，链路两端的交换机端口都需要配置
# 1. 将端口设置为中继模式
[sw1]int g0/0/24
[sw1-GigabitEthernet0/0/24]port link-type trunk

# 2. 设置中继端口允许哪些VLAN的数据通过
[sw1-GigabitEthernet0/0/24]port trunk all-pass vlan all
```

## 链路聚合

- 交换机之间可以连接多条链路
- 将多条链路捆绑成一个逻辑端口，以提供更大的带宽，同时可以实现容错
- 注意
  - 参与捆绑的所有端口需要有一致的物理状态，如都是1000Mb/s
  - 参与捆绑的所有端口要么同属于同一VLAN，要么都是中继

```shell
# 1. 清除参与捆绑端口的配置
[sw1]clear configuration interface GigabitEthernet 0/0/23
[sw1]clear configuration interface GigabitEthernet 0/0/24
# 2. 创建名为Eth-Trunk 0的逻辑端口
[sw1]interface Eth-Trunk 0
# 3. 把物理端口加入到逻辑端口中
[sw1-Eth-Trunk0]trukport GigabitEthernet 0/0/23 0/0/24
# 4. 配置逻辑端口为中继状态
[sw1-Eth-Trunk0]port link-type trunk
[sw1-Eth-Trunk0]port trunk allow-pass vlan all
# 5. 将物理端口启用
[sw1]interface GigabitEthernet 0/0/23
[sw1－GigabitEthernet0/0/23]undo shutdown
[sw1]interface GigabitEthernet 0/0/24
[sw1－GigabitEthernet0/0/24]undo shutdown
# 6. 查看
[sw1]display vlan
[sw1]display interface Eth-Trunk 0
[sw1]display current-configuration
```

## 网络层

- IP地址：32位2进制数。
  - 私有地址
    - 10.0.0.0/8
    - 172.16.0.0 - 172.31.0.0/16
    - 192.168.0.0 - 192.168.255.0/24
- 路由器：
  - 路由：路径
  - 路由器：负责路径选择的设备

- ARP：地址解析协议
  - 三层需要IP地址
  - 二层需要MAC地址
  - ARP协议用于将IP地址解析为MAC地址

### 路由器工作原理

- 路由器负责将不同的网络连接起来；交换机连接的是相同网络
- 路由器是三层设备，它的每个端口都有IP地址
- 路由器收到数据包后，根据自己的路由表做出转发决定
- 如果目的地不在路由表中，则将数据包丢弃
- 路由器不允许广播通过
- 路由表的形成可以是管理员手工配置静态路由；也可以通过路由协议自动学习
- 路由表中保存的是最优路径，而不是全部路径

```shell
[R1]display interface brief  # 查看端口简要信息
[R1]display ip routing-table  # 查看路由表
[R1]int g0/0/0
[R1-GigabitEthernet 0/0/0]ip address 192.168.1.1 24  # 配置IP地址
[R1]display ip routing-table  # 配置IP地址后，路由表中将出现直连路由
[R1]ip route-static 目标网络 目标掩码 下一跳地址
[R1]ip route-static 192.168.3.0 24 192.168.2.2

# 缺省路由，也叫默认路由。不管目标是哪，下一跳一样，采用默认路由
[R1]ip route-static 0.0.0.0 0 下一跳
[R1]ip route-static 0.0.0.0 0 192.168.2.2
```









