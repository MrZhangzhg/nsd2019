# py02_day04

## re模块

```python
>>> import re
# 在进行匹配的时候，如果匹配到了，返回匹配对象，否则返回None
>>> re.match('f..', 'food')
<_sre.SRE_Match object; span=(0, 3), match='foo'>
>>> re.match('f..', 'seafood')
>>> print(re.match('f..', 'seafood'))
None

>>> re.search('f..', 'food')
<_sre.SRE_Match object; span=(0, 3), match='foo'>
>>> re.search('f..', 'seafood')
<_sre.SRE_Match object; span=(3, 6), match='foo'>
>>> m = re.search('f..', 'seafood')
>>> m.group()   # 返回匹配到的内容
'foo'

>>> re.search('f..', 'seafood is food')
<_sre.SRE_Match object; span=(3, 6), match='foo'>
>>> m = re.search('f..', 'seafood is food')
>>> m.group()
'foo'
>>> re.findall('f..', 'seafood is food')
['foo', 'foo']

>>> list(re.finditer('f..', 'seafood is food'))
[<_sre.SRE_Match object; span=(3, 6), match='foo'>, <_sre.SRE_Match object; span=(11, 14), match='foo'>]
>>> for m in re.finditer('f..', 'seafood is food'):
...     print(m.group())
... 
foo
foo
```







