# nsd1906_devweb_day01

python与运维相关的模块：shutil、os、subprocess、sys、hashlib、tarfile、smtplib、paramiko、IPy(计算IP地址)、psutil(获取主机资源信息)、libvirt-python(管理虚拟机)

## web开发

web前端：html、CSS、javascript

web后台：python、php、java等

## HTML

- 超文本标记语言
- 它使用标记形成文档的结构
- 它不是可见即可用的

## 标记

- 也叫标签、元素
- 分为双标记，如\<h1\>一号标题\</h1\>；和单标记，如\<hr\>
- 标记分为
  - 块级元素：至少要占一行，如h1-h6，p、div、ul、ol
  - 行内元素：不产生换行，如span、i、b等

- html是根标记，它一般包括两个直接子元素head和body
  - head可以设置一些属性以及title
  - 出现在浏览器窗口中的内容写到body中

- 标记还可以嵌套
- 注释采用：\<!--    --\>

### URL：统一资源定位符

w3school: https://www.w3school.com.cn/



## CSS：层叠样式表

例：

```python
# 下载腾讯首页
>>> import wget
>>> wget.download('http://www.qq.com', '/tmp/qq.html')
# firefox打开文件时，发现乱码
(nsd1906) [root@room8pc16 day01]# firefox /tmp/qq.html 
# 查看文件类型，发现它其实是gzip压缩文件
(nsd1906) [root@room8pc16 day01]# file /tmp/qq.html 
/tmp/qq.html: gzip compressed data, from Unix
# 解压
(nsd1906) [root@room8pc16 day01]# mv /tmp/qq.html /tmp/qq.html.gz
(nsd1906) [root@room8pc16 day01]# gzip -d /tmp/qq.html.gz
(nsd1906) [root@room8pc16 day01]# ls /tmp/qq.html 
/tmp/qq.html
(nsd1906) [root@room8pc16 day01]# file /tmp/qq.html
(nsd1906) [root@room8pc16 day01]# firefox /tmp/qq.html

# 修改样式表说明
[root@room8pc16 myansible]# vim /tmp/qq.html # 样式表路径加上http:
<link rel="stylesheet" href="http://mat1.xxxxxxxxxxxxxxx
```

- 也叫级联式表，简称样式表
- 样式表的类型
  - 内联样式，与标签属性一样，直接应用在标签上。不推荐
  - 内部样式，将样式统一写在head标签中
  - 外部样式，将样式集中放在一个样式表文件中

