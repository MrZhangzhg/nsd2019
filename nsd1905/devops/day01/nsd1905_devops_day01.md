# nsd1905_devops_day01

## 多进程

多进程使用os.fork()实现

os.fork()的返回值是数字，这个数字在父进程中是非0值（子进程的PID），在子进程中为0。

多进程的编程思路：

- 父进程仅用于生成子进程
- 子进程做具体的工作
- 子进程工作完成后，务必退出




