Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Rectangle:
	def __init__(self,x,y):
		self.x=x
		self.y=y

	
>>> class Rectangle:
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def getPeri(self):
		return (self.x+self.y)*2
	def getArea(self):
		return self.x *self.y

	
>>> rect=Rectangle()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    rect=Rectangle()
TypeError: __init__() missing 2 required positional arguments: 'x' and 'y'
>>> rect=Rectangle(3,4)
>>> rect.getPeri()
14
>>> rect.getArea()
12
>>> class A :
	def __init__(self):
		return 'A fo A-Cup'

	
>>> a=A()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a=A()
TypeError: __init__() should return None, not 'str'
>>> 
>>> class CapStr(str):
	def __new__(cls,string):
		string = string.upper()
		return str.__new__(cls,string)

	
>>> a=CapStr('i love owen')
>>> a
'I LOVE OWEN'
>>> 
>>> class C:
	def __init__(self):
		print('我是__init__方法，我被调用了...')
	def __init__(self):
		print('我是__del__方法，我被调用了...')

		
>>> c1=C()
我是__del__方法，我被调用了...
>>> class C:
	def __init__(self):
		print('我是__init__方法，我被调用了...')
	def __del__(self):
		print('我是__del__方法，我被调用了...')

		
>>> c2=C()
我是__init__方法，我被调用了...
>>> c3=c2
>>> c4=c3
>>> del c3
>>> del c2
>>> del c4
我是__del__方法，我被调用了...
>>> #对象生成以后，所有对它的引用被删除以后，才会启动垃圾回收机制
>>> #就是没有了映射对应过去，就删除了
>>> 
>>> 
>>> #魔法方法
>>> type(len)
<class 'builtin_function_or_method'>
>>> type(dir)
<class 'builtin_function_or_method'>
>>> type(int)
<class 'type'>
>>> type(list)
<class 'type'>
>>> class C:
	pass

>>> type(C)
<class 'type'>
>>> a=int('123')
>>> a
123
>>> b=int('457')
>>> a+b
580
>>> 
>>> class New_init(int):
	def __add__(self,other):
		return int.__sub__(self,other)
	def __sub__(self,other):
		return int.__add__(self,other)

	
>>> a=New_int(3)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    a=New_int(3)
NameError: name 'New_int' is not defined
>>> a=New_int()
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a=New_int()
NameError: name 'New_int' is not defined
>>> class Newinit(int):
	def __add__(self,other):
		return int.__sub__(self,other)
	def __sub__(self,other):
		return int.__add__(self,other)

	
>>> a=New_int(3)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    a=New_int(3)
NameError: name 'New_int' is not defined
>>> class  Newinit(int):
	def __add__(self,other):
		return int.__sub__(self,other)
	def __sub__(self,other):
		return int.__add__(self,other)

	
>>> a=New_int(3)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    a=New_int(3)
NameError: name 'New_int' is not defined
>>> a=Newint(3)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a=Newint(3)
NameError: name 'Newint' is not defined
>>> class  New_int(int):
	def __add__(self,other):
		return int.__sub__(self,other)
	def __sub__(self,other):
		return int.__add__(self,other)

	
>>> a=New_int(3)
>>> b=New_int(5)
>>> a+b
-2
>>> a-b
8
>>> 
>>> class Try_int(int)
SyntaxError: invalid syntax
>>> class Try_int(int):
	def __add__(self,other):
		return self + other
	def __sub__(self,other):
		return self - other

	
>>> a=Try_int(3)
>>> b=Try_int(4)
>>> a+b
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    a+b
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
  File "<pyshell#90>", line 3, in __add__
    return self + other
RecursionError: maximum recursion depth exceeded
>>> class Try_int(int):
	def __add__(self,other):
		return int(self) + int(other)
	def __sub__(self,other):
		return int(self) - int(other)

	
>>> a=Try_int(3)
>>> b=Try_int(5)
>>> b+a
8
>>> 
>>> #魔法方法
>>> class int(int):
	def __add__(self,other):
		return int.__sub__(self,other)

	
>>> a=int('5')
>>> a
5
>>> b = int(3)
>>> a+b
2
>>> 
=============================== RESTART: Shell ===============================
>>> class Nint(int):
	def __radd__(self,other):
		return int.sub__(self,other)

	
>>> a=Nint(5)
>>> b=Nint(3)
>>> a+b
8
>>> 1+b
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    1+b
  File "<pyshell#112>", line 3, in __radd__
    return int.sub__(self,other)
AttributeError: type object 'int' has no attribute 'sub__'
>>> class Nint(int):
	def __radd__(self,other):
		return int.__sub__(self,other)

	
>>> 1+b
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    1+b
  File "<pyshell#112>", line 3, in __radd__
    return int.sub__(self,other)
AttributeError: type object 'int' has no attribute 'sub__'
>>> b=Nint(3)
>>> a=Nint(5)
>>> a+b
8
>>> 1+b
2
>>> 
=============================== RESTART: Shell ===============================
>>> class Nint(int):
	def __rsub__(self,other):
		return int.__sub__(self,other)

	
>>> a=Nint(5)
>>> 3=a
SyntaxError: can't assign to literal
>>> 3-a
2
>>> class Nint(int):
	def __rsub__(self,other):
		return int.__sub__(other,self)

	
>>> a=Nint(4)
>>> 6-a
2
>>> 
