# nsd1903_python1_day01

## 环境准备

官方站点：http://www.python.org

IDE：集成开发环境

### pycharm的配置

1. 如果是第一次使用，打开后，出现以下内容，选择下面的“不导入配置”

![1564537055280](/root/.config/Typora/typora-user-images/1564537055280.png)

2. 如果是专业版，需要购买

![1564537199490](/root/.config/Typora/typora-user-images/1564537199490.png)

3. 选择界面风格

![1564537283001](/root/.config/Typora/typora-user-images/1564537283001.png)

4. 创建新项目，一个软件工程就是一个项目，对应一个文件夹

![1564537362824](/root/.config/Typora/typora-user-images/1564537362824.png)

5. 创建虚拟环境

Location: 项目目录，即代码文件存放的路径

Project Interpreter：解释器采用虚拟环境，相当于是把系统的python程序拷贝到了一个文件夹中，以后安装python软件都安装到这个文件夹。将来项目完成了，不需要这个环境了，只要把虚拟环境目录删除即可。

![1564537523333](/root/.config/Typora/typora-user-images/1564537523333.png)

6. 如果上一步，自动创建虚拟环境出现故障，可以手工创建虚拟环境

```shell
# 创建虚拟环境
[root@room8pc16 nsd1903]# python3 -m venv ~/nsd1903
# 使用虚环境时，需要激活它
[root@room8pc16 nsd1903]# source ~/nsd1903/bin/activate
(nsd1903) [root@room8pc16 nsd1903]# python --version
Python 3.6.7
```

7. 修改pycharm项目的虚拟环境

File -> Settings -> Project: Day01 -> Project Interpreter -> 点右上角的齿轮 -> Add Local ->   Existing Enviroment -> 点击... -> 输入/root/nsd1903/bin/python

![1564538156502](/root/.config/Typora/typora-user-images/1564538156502.png)

![1564538286662](/root/.config/Typora/typora-user-images/1564538286662.png)

8. 修改编辑文字大小

File -> Settings -> Editor -> font -> size 修改大小

