一：
#自己解决问题Python的方法
>>> #
>>> #1.可以去IDLE的help，然后就去索引模块
>>> #然后就是：
>>> #例子
>>> import timeit
>>> timeit.__doc__

二：
#看有哪些函数，方法
>>> dir(timeit)
['Timer', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_globals', 'default_number', 'default_repeat', 'default_timer', 'dummy_src_name', 'gc', 'itertools', 'main', 'reindent', 'repeat', 'sys', 'template', 'time', 'timeit']
>>> #过滤掉渣渣
>>> timeit.__all__
['Timer', 'timeit', 'repeat', 'default_timer']
>>> #上面的四个就是作者希望别人调用的函数或者方法
>>> from timeit import *
>>> Timer
<class 'timeit.Timer'>
>>> #比如gc就没有
>>> gc
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    gc
NameError: name 'gc' is not defined



三：看别人的代码
import timeit
>>> timeit.__file__
'C:\\Users\\Administrator\\AppData\\Python\\Python35-32\\lib\\timeit.py'

四：
>>> help(timeit)



自己写+看别人+没了
