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



### python运行方式

- 交互解释器

```python
[root@room8pc16 devops0101]# source ~/nsd1903/bin/activate
(nsd1903) [root@room8pc16 devops0101]# python
>>> print("hello world!")
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
```

- 文件形式
在pycharm项目名上右击选第四项，可以拷贝到项目的绝对路径

```python
# vim hi.py
print("Hello World!")
(nsd1903) [root@room8pc16 day01]# python hi.py 
Hello World!
```

### python语法

- python使用缩进表达代码逻辑，推荐缩进4个空格
- 有子语句的代码，后面都有冒号
- 注释使用＃号，在pycharm中可以按ctrl + /进行注释或取消注释
- 多个语句在同一行，需要使用分号分隔，但是仍然不推荐。

### 输入输出语句

```python
# 字符串必须写在引号中，单双引号没有区别
>>> print('hello world!')
# 一个print语句中，可以打印多项，123没有引号，表示数字。默认各项间用空格分隔
>>> print('hao', 123, 'world')
hao 123 world
# 输出时，也可以指定各项之间的分隔符
>>> print('hao', 123, 'world', sep='_')
hao_123_world
>>> print('hao', 123, 'world', sep='***')
hao***123***world
# 字符串可以使用+拼接 
>>> print('hello' + 'world')
helloworld

# 通过input获取键盘输入，input括号中的字符串是屏幕提示符，把用户输入的结果保存在变量num中，num是变量，使用时不用像shell那样加$前缀。
>>> num = input("number: ")
number: 100
>>> num
'100'
# 只要通过input读取，都是字符类型，字符不能和数字进行四则运算
>>> num + 10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str, not int

# 可以通过int函数把num转换成整数，再和数字进行运算
>>> int(num) + 10
110
```







