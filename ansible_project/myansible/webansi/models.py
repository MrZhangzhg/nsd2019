from django.db import models

class HostGroup(models.Model):
    groupname = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self):
        return '组: %s' % self.groupname

class Host(models.Model):
    hostname = models.CharField(max_length=100, unique=True, null=False)
    ipaddr = models.CharField(max_length=15, unique=True, null=False)
    group = models.ForeignKey(HostGroup, on_delete=models.CASCADE)

    def __str__(self):
        return '%s=> %s' % (self.hostname, self.group)

class Module(models.Model):
    modulename = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self):
        return '模块: %s' % self.modulename

class Argument(models.Model):
    arg_text = models.CharField(max_length=200, unique=True, null=False)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return '%s=> %s' % (self.module, self.arg_text)
