Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #函数之，我的地盘听我的
>>> def discounts(price,rate):
	final price=price*rate
	
SyntaxError: invalid syntax
>>> def discounts(price,rate):
	final price =price*rate
	
SyntaxError: invalid syntax
>>> def discounts(price,rate):
	final_price =price*rate
	return final_price
old_price =float (input('请输入原价'))
SyntaxError: invalid syntax
>>> def discounts(price,rate):
	final_price =price*rate
	return final_price =float (input('请输入原价'))
SyntaxError: invalid syntax
>>> def discounts(price,rate):
	final_price =price*rate
	return final_price =float (input('请输入原价'))
SyntaxError: invalid syntax
>>> def discounts(price,rate):
	final_price =price*rate
	return final_price
old_price=float (input('请输入原价'))
SyntaxError: invalid syntax
>>> def discounts(price,rate):
	final_price =price*rate
	return final_price
    old_price=float (input('请输入原价'))
    
SyntaxError: unindent does not match any outer indentation level
>>> def discounts(price,rate):
	final_price =price*rate
	return final_price
    old_price=float (input('请输入原价'))
    
SyntaxError: unindent does not match any outer indentation level
>>> def discounts(price,rate):
	final_price =price*rate
	return final_price
old_price=float (input('请输入原价
		       
SyntaxError: invalid syntax
>>> cls
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    cls
NameError: name 'cls' is not defined
>>> clear
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> 
================ RESTART: D:/Python_program/jububianliang.py ================
请输入原价
================ RESTART: D:/Python_program/jububianliang.py ================
请输入原价:100
请输入折扣率0.8
打折后的价格是： 80.0
>>> 
================ RESTART: D:/Python_program/jububianliang.py ================
请输入原价:100
请输入折扣率0.8
打折后的价格是： 80.0
Traceback (most recent call last):
  File "D:/Python_program/jububianliang.py", line 10, in <module>
    print('这里师徒打印局部变量final_price的值：',final_price)
NameError: name 'final_price' is not defined
>>> 
================ RESTART: D:/Python_program/jububianliang.py ================
请输入原价:
================ RESTART: D:/Python_program/jububianliang.py ================
请输入原价:100
请输入折扣率.08
这里试图打印全局变量的值： 100.0
打折后的价格是： 8.0
>>> 
================ RESTART: D:/Python_program/jububianliang.py ================
请输入原价:100
请输入折扣率0.8
修改后的old_price的值是1： 50
打折后的价格是： 80.0
>>> 
================ RESTART: D:/Python_program/jububianliang.py ================
请输入原价:100
请输入折扣率0.8
修改后的old_price的值是1： 50
修改后的old-price的值是2： 100.0
打折后的价格是： 80.0
>>> 
>>> 
>>> count=5
>>> def MyFun():
	count=10
	print(10)

	
>>> MyFun()
10
>>> print(count)
5
>>> def MyFun():
	count=10
	print(count)

	
>>> print(count)
5
>>> MyFun()
10
>>> def MyFun():
	global count
	count=10
	print(count)

	
>>> MyFun()
10
>>> print(count)
10
>>> #内嵌函数
>>> 
>>> 
>>> def fun1():
	print('fun1()正在被调用。。。')
	def fun2():
		print('fun2()正在被调用。。。')
	fun2()

	
>>> fun1()
fun1()正在被调用。。。
fun2()正在被调用。。。
>>> 
>>> def fun1():
{	print('fun1()正在被调用。。。')
	def fun2():
		print('fun2()正在被调用。。。')
	fun2()}
SyntaxError: expected an indented block
>>> def fun1():
{	print('fun1()正在被调用。。。')
	def fun2():
		print('fun2()正在被调用。。。')
	fun2()}
SyntaxError: expected an indented block
>>> 
>>> 
>>> 
>>> 
>>> fun2()
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    fun2()
NameError: name 'fun2' is not defined
>>> 
>>> 
>>> #闭包
>>> def FunX(x)
SyntaxError: invalid syntax
>>> def FunX(x):
	def FunY(y):
		return x*y
	return FunY

>>> i=FunX(8)
>>> i
<function FunX.<locals>.FunY at 0x03A08B70>
>>> type(i)
<class 'function'>
>>> i(5)
40
>>> FunX(8)(4)
32
>>>  FunX(5,5)
 
SyntaxError: unexpected indent
>>> FunX(5)(5)
25
>>> FunY(5)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    FunY(5)
NameError: name 'FunY' is not defined
>>> Funx(5)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    Funx(5)
NameError: name 'Funx' is not defined
>>> FunX(5)
<function FunX.<locals>.FunY at 0x03A08C00>
>>> def Fun1():
	x=[5]
	def Fun2():
		x[0] *=x[0]
		return x[0]
	return Fun2()

>>> Fun1()
25
>>> #上面那个例子能成是因为x=[5]
>>> #是一个列表，不存放在栈里面，所以不会有全局，局部变量的问题
>>> 
>>> def Fun1():
	x=5
	def Fun2():
               nonlocal x
		x* =x
		return x[0]
	return Fun2()
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> def Fun1():
	x=5
	def Fun2():
               nonlocal x
		x *=x
		return x[0]
	return Fun2()
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> def Fun1():
	x=5
	def Fun2():
                nonlocal x
		x *=x
		return x[0]
	return Fun2()
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> def Fun1():
	x=5
	def Fun2():
                nonlocal x
		x *=x
		return x[0]
	return Fun2()
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> 
>>> def Fun1():
	x=5
	def Fun2():
                nonlocal x
		x *=x
		return x[0]
	return Fun2()
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> 
>>> 
>>> #lambda,,匿名函数
>>> 
>>> 
>>> 
>>> 
>>> def d5(x):
	return 2* x +1

>>> ds(2)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    ds(2)
NameError: name 'ds' is not defined
>>> d5(2)
5
>>> lambda x:2*x+1
<function <lambda> at 0x03A08CD8>
>>> type(lambda)
SyntaxError: invalid syntax
>>> #是一个列表，不存放在栈里面，所以不会有全局，局部变量的问题
KeyboardInterrupt
>>> g=lambda x:2*x +1
>>> g(5)
11
>>> 
>>> add=lambda x,y:x+y
>>> add(3,6)
9
>>> #使用Python写一些执行脚本的时候，用lambda就可以省去定义函数的过程
>>> 
>>> 
>>> filter(None,[1,0,False,Ture])
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    filter(None,[1,0,False,Ture])
NameError: name 'Ture' is not defined
>>> filter(None,[1,0,False,True])
<filter object at 0x03A0E490>
>>> list(filter(None,[1,0,False,True]))
[1, True]
>>> def odd(x):
	return x%2

>>> temp=range(10)
>>> show=filter(odd,temp)
>>> list(show)
[1, 3, 5, 7, 9]
>>> print max(filter(lambda x: 555555 % x == 0, range(100, 999)))
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> list(filter(lambda x: x%2==0,range(10)))
[0, 2, 4, 6, 8]
>>> 
>>> list(map(lambda x:x*2，range(10)))
SyntaxError: invalid character in identifier
>>> list(map(lambda x:x*2, range(10)))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
>>> 
>>> 
>>> #什么是递归
>>> 
>>> 
>>> 
>>> def recursion():
	return recursion()

>>> #设置递归层数
>>> import sys
>>> 
 RESTART: C:/Users/Administrator/AppData/Local/Programs/Python/Python35-32/factorial.py 
please enter a number:6
%d 的阶乘
>>> 
 RESTART: C:/Users/Administrator/AppData/Local/Programs/Python/Python35-32/factorial.py 
please enter a number:6
Traceback (most recent call last):
  File "C:/Users/Administrator/AppData/Local/Programs/Python/Python35-32/factorial.py", line 10, in <module>
    print("%d 的阶乘"(number,result))
TypeError: 'str' object is not callable
>>> 
 RESTART: C:/Users/Administrator/AppData/Local/Programs/Python/Python35-32/factorial.py 
please enter a number:6
6 的阶乘6
>>> 
 RESTART: C:/Users/Administrator/AppData/Local/Programs/Python/Python35-32/factorial.py 
please enter a number:5
5 的阶乘5
>>> 
 RESTART: C:/Users/Administrator/AppData/Local/Programs/Python/Python35-32/factorial.py 
please enter a number:5
5 的阶乘5
>>> 
 RESTART: C:/Users/Administrator/AppData/Local/Programs/Python/Python35-32/factorial.py 
please enter a number:6
6 的阶乘6
>>> 
 RESTART: C:/Users/Administrator/AppData/Local/Programs/Python/Python35-32/factorial.py 
please enter a number:5
5 的阶乘5
>>> 
 RESTART: C:/Users/Administrator/AppData/Local/Programs/Python/Python35-32/factorial.py 
please enter a number:4
Traceback (most recent call last):
  File "C:/Users/Administrator/AppData/Local/Programs/Python/Python35-32/factorial.py", line 10, in <module>
    print("%d 的阶乘%d"% number %result)
TypeError: not enough arguments for format string
>>> 
 RESTART: C:/Users/Administrator/AppData/Local/Programs/Python/Python35-32/factorial.py 
please enter a number:5
Traceback (most recent call last):
  File "C:/Users/Administrator/AppData/Local/Programs/Python/Python35-32/factorial.py", line 10, in <module>
    print("%d 的阶乘 %d" %number %result)
TypeError: not enough arguments for format string
>>> 
 RESTART: C:/Users/Administrator/AppData/Local/Programs/Python/Python35-32/factorial.py 
please enter a number:5
Traceback (most recent call last):
  File "C:/Users/Administrator/AppData/Local/Programs/Python/Python35-32/factorial.py", line 10, in <module>
    print("%d 的阶乘 %d" %number %result)
TypeError: not enough arguments for format string
>>> 
 RESTART: C:/Users/Administrator/AppData/Local/Programs/Python/Python35-32/factorial.py 
please enter a number:6
6 的阶乘 6
>>> 
 RESTART: C:/Users/Administrator/AppData/Local/Programs/Python/Python35-32/factorial.py 
please enter a number:2
2 的阶乘 2
>>> 
 RESTART: C:/Users/Administrator/AppData/Local/Programs/Python/Python35-32/factorial.py 
please enter a number:5
5 的阶乘 5
>>> 
 RESTART: C:/Users/Administrator/AppData/Local/Programs/Python/Python35-32/factorial.py 
please enter a number:5
 的阶乘 5
>>> 
 RESTART: C:/Users/Administrator/AppData/Local/Programs/Python/Python35-32/factorial.py 
please enter a number:5
 的阶乘 120.
>>>  
