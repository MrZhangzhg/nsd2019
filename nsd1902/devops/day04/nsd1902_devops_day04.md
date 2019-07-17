# nsd1902_devops_day04

## ansible模块练习

1. 环境变量

   ```python
   # export ANSIBLE_LIBRARY=/opt/myansible_lib/
   ```

2. 编写模块

   ```python
   # vim /opt/myansible_lib/download.py 
   #!/usr/bin/env python
   # -*- coding: utf8 -*-
   '用于下载指定文件'
   
   from ansible.module_utils.basic import AnsibleModule
   import wget
   
   def main():
       module = AnsibleModule(
           argument_spec=dict(
               url=dict(required=True, type='str'),
               path=dict(required=True, type='str')
           )
       )
       wget.download(module.params['url'], module.params['path'])
       module.exit_json(changed=True)
   
   if __name__ == '__main__':
       main()
   ```

   > 注意：远程主机只有python2，不是python3。python2默认字符采用的是ASCII码，而不是unicode，所以python2的文本中不能写汉字。如果需要添加汉字，需要在文件中指定字符集。

3. 在远程主机上安装wget。因为ansible准备好的模块，需要在远程主机上执行。

   ```shell
   # 在本机上下载wget
   # pip3 download wget --trusted-host pypi.douban.com
   
   # 在远程主机上安装wget
   # ansible webservers -m copy -a "src=files/wget-3.2.zip dest=/root"
   # ansible webservers -m shell -a "cd /root; unzip wget-3.2.zip"
   # ansible webservers -m shell -a "cd /root/wget-3.2/; python setup.py install"
   ```

4. 通过自己编写的模块，下载文件

   ```python
   # ansible webservers -m download -a "url=http://192.168.4.254/zabbix.png path=/tmp/zabbix.png"
   ```

   