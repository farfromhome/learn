Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/Administrator/AppData/Python/Python35-32/python_program/类1.py 
>>> tt=Turtle()
>>> tt.climb()
我正在很努力的向前爬......
>>> tt.bite()
有得吃,真满足^_^
>>> tt.sleep
<bound method Turtle.sleep of <__main__.Turtle object at 0x036DCA70>>
>>> tt.sleep()
困了,睡了,晚安,Zzzz
>>> list1=[2,1,4,5]
>>> list1.sort()
>>> list1
[1, 2, 4, 5]
>>> list.append(9)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    list.append(9)
TypeError: descriptor 'append' requires a 'list' object but received a 'int'
>>> list1.append(9)
>>> 
>>> list1
[1, 2, 4, 5, 9]
>>> class MyList(list):
	pass

>>> list2=MyList()
>>> list2.append(5)
>>> list2.append(3)
>>> list2.append(7)
>>> list2
[5, 3, 7]
>>> list2.sort()
>>> list3.append(2)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    list3.append(2)
NameError: name 'list3' is not defined
>>> list3
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    list3
NameError: name 'list3' is not defined
>>> list=list3
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    list=list3
NameError: name 'list3' is not defined
>>> list3=list
>>> list3.append(3)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    list3.append(3)
TypeError: descriptor 'append' requires a 'list' object but received a 'int'
>>> list3
<class 'list'>
>>> list3=[3,3,54,5]
>>> list3.append(0)
>>> list3
[3, 3, 54, 5, 0]
>>> list3.sort()
>>> list
<class 'list'>
>>> list3
[0, 3, 3, 5, 54]
>>> class A:
	def fun(self):
		print('我是小a')

		
>>> class B:
	def fun(self):
		print('我是小b')

		
>>> a.fun()
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a.fun()
NameError: name 'a' is not defined
>>> a=A
>>> a.fun()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a.fun()
TypeError: fun() missing 1 required positional argument: 'self'
>>> a=A()
>>> a.fun()
我是小a
>>> b=B()
>>> b.fun()
我是小b
>>> 
>>> 
>>> #对象和类
>>> 
>>> class Ball:
	def setName(self,name):
		self.name=name
	def kick(self):
		print('我叫%，该死的，谁踢我...'%self.name)

		
>>> a=Ball()
>>> a.setName('球a')
>>> b=Ball()
>>> b.setName('球B')
>>> c=Ball()
>>> c.setName('优酷')
>>> a.kick(0
       
KeyboardInterrupt
>>> a.kick()
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a.kick()
  File "<pyshell#57>", line 5, in kick
    print('我叫%，该死的，谁踢我...'%self.name)
ValueError: unsupported format character '?' (0xff0c) at index 3
>>> class Ball:
	def setName(self,name):
		self.name=name
	def kick(self):
		print('我叫%s，该死的，谁踢我...'%self.name)

		
>>> a.kick()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    a.kick()
  File "<pyshell#57>", line 5, in kick
    print('我叫%，该死的，谁踢我...'%self.name)
ValueError: unsupported format character '?' (0xff0c) at index 3
>>> class Ball:
	def setName(self,name):
		self.name=name
	def kick(self):
		print('我叫%s，该死的，谁踢我...'% self.name)

		
>>> a=Ball()
>>> a.setName('a')
>>> b=Ball(0
       
KeyboardInterrupt
>>> a.kick()
我叫a，该死的，谁踢我...
>>> b=Ball()
>>> b.setName('习近平')
>>> b.kick()
我叫习近平，该死的，谁踢我...
>>> class Ball:
	def __init__(self,name):
		self.name=name

		
>>> class Ball:
	def __init__(self,name):
		self.name=name
	def kick(self):
		print('我叫%，该死的，谁踢我...'% self.name)

		
>>> b=Ball('土豆')
>>> b.kick()
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    b.kick()
  File "<pyshell#85>", line 5, in kick
    print('我叫%，该死的，谁踢我...'% self.name)
ValueError: unsupported format character '?' (0xff0c) at index 3
>>> class Ball:
	def __init__(self,name):
		self.name=name
	def kick(self):
		print('我叫%s，该死的，谁踢我...'% self.name)

		
>>> b=Ball('土豆')
】
>>> b.kick(0
       
KeyboardInterrupt
>>> b.kick()
我叫土豆，该死的，谁踢我...
>>> c=Ball()
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    c=Ball()
TypeError: __init__() missing 1 required positional argument: 'name'
>>> class Person:
	name='Owen'

	
>>> p=Person()
>>> 
>>> p.name
'Owen'
>>> class Person:
	name='Owen'

	
>>> p=Person
>>> p=Person()
>>> p.name
'Owen'
>>> class Person:
	__name='Owen'

	
>>> p=Person()
>>> p.name
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    p.name
AttributeError: 'Person' object has no attribute 'name'
>>> class Person:
	__name='Owen'
	def getName(self):
		return self.__name

	
>>> p=Person()
>>> p.__name
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    p.__name
AttributeError: 'Person' object has no attribute '__name'
>>> p.getName()
'Owen'
>>> #__就是python 改了一下名字，改成了_类名_变量名
>>> #可以这样访问
>>> 
>>> p._
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    p._
AttributeError: 'Person' object has no attribute '_'
>>> p._Person_name
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    p._Person_name
AttributeError: 'Person' object has no attribute '_Person_name'
>>> class Person:
	__name='Owen'
	def getName(self):
		return self.__name

	
>>> p._Person_name
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    p._Person_name
AttributeError: 'Person' object has no attribute '_Person_name'
>>> p._Person__name
'Owen'
>>> 
>>> 
>>> 
>>> class Parent:
	def hello(self):
           print('正在调用父类的方法...')

           
>>> class Child(Parent):
	pass

>>> p=Parent()
>>> p.hello()
正在调用父类的方法...
>>> c=Child()
>>> c.hello()
正在调用父类的方法...
>>> 
>>> #如果子类中定义与弗雷同名的方法或属性，则会自动覆盖弗雷对应的方法或属性。
>>> 
>>> class Child(Parent):
	def hello(self):
		print('正在调用子类的方法...')

		
>>> c=Child()
>>> c.hello
<bound method Child.hello of <__main__.Child object at 0x036E4690>>
>>> c.hello()
正在调用子类的方法...
>>> p.hello()
正在调用父类的方法...
>>> 
 RESTART: C:/Users/Administrator/AppData/Python/Python35-32/python_program/fish.py 
>>> fish=Fish()
>>> fish.goldfish()
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    fish.goldfish()
AttributeError: 'Fish' object has no attribute 'goldfish'
>>> fish.Goldfish()
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    fish.Goldfish()
AttributeError: 'Fish' object has no attribute 'Goldfish'
>>> fish.move()
我的位置是： 6 2
>>> fish.move()
我的位置是： 5 2
>>> fish.move()
我的位置是： 4 2
>>> Goldfish=Goldfish()
>>> Goldfish.move()
我的位置是： -1 7
>>> Goldfish.move()
我的位置是： -2 7
>>> shark=Shark()
>>> shark.eat()
吃货的梦想就是天天有的吃^_^
>>> shark.eat()
太撑了，吃不下了！
>>> shark.eat()
太撑了，吃不下了！
>>> shark.move()
我的位置是： 9 6
>>> shark.move()
我的位置是： 8 6
>>> 
>>> 
>>> #多重继承
>>> class Base1:
	def foo1(self):
		print('我是foo1,我为Base1代言')

		
>>> class Base2:
	def foo2(self):
		print('我是foo2,我为Base2代言...')

		
>>> class c(Base1,Base2)
SyntaxError: invalid syntax
>>> class C(Base1,Base2)
SyntaxError: invalid syntax
>>> class C(Base1,Base2)
SyntaxError: invalid syntax
>>> class Base1:
	def foo1(self):
		print('我是foo1,我为Base1代言')


>>> class C(Base1)
SyntaxError: invalid syntax
>>> class C (Base1)
SyntaxError: invalid syntax
>>> class C (Base1,Base2):
	pass

>>> c=C
>>> c.foo1
<function Base1.foo1 at 0x034B1CD8>
>>> c.foo1()
Traceback (most recent call last):
  File "<pyshell#192>", line 1, in <module>
    c.foo1()
TypeError: foo1() missing 1 required positional argument: 'self'
>>> c=C()
>>> c.foo1()
我是foo1,我为Base1代言
>>> 
