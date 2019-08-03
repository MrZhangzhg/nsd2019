import shutil

f1 = open('/etc/passwd', 'rb')
f2 = open('/tmp/mima', 'wb')

shutil.copyfileobj(f1, f2)
f1.close()
f2.close()

shutil.copyfile()
shutil.copy2()
