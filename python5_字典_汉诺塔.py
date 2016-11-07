def move(n, a, buffer, c):
    if(n == 1):
        print(a,"->",c)
        return
    move(n-1, a, c, buffer)
    move(1, a, buffer, c)
    move(n-1, buffer, a, c)
move(3, "a", "b", "c")





def hanoi(n,x,y,z ):
     if n==1:
        print(x, '-->',z)

     else:
        hanoi(n-1,x,y,z)   #将前n-1个盘子从x移动到y上
        print(x, '-->', z) #将最底下的最后一个盘子从x移动到z上
        hanoi(n-1,y,x,z)   #将y上的n-1个盘子移动到z上




n=int(input('please input layer number'))
hanoi(n,'X','Y','Z')

please input layer number3
X --> Z
hello
X --> Y
Z --> Y
hello
X --> Z
Y --> X
hello
Y --> Z
X --> Z
>>> brand =['李宁'，'李宁','阿迪达斯','鱼鱼工作室']
SyntaxError: invalid character in identifier
>>> brand =['李宁','李宁','阿迪达斯','鱼鱼工作室']
>>> slogan=['一切皆有可能','Just do it','Nothing is impossible','让编程改变世界']
>>> print('鱼鱼工作室的的口号是：'，slogan[brand.index('鱼鱼工作室')])
SyntaxError: invalid character in identifier
>>> print('鱼鱼工作室的的口号是：',slogan[brand.index('鱼鱼工作室')])
鱼鱼工作室的的口号是： 让编程改变世界
>>> dirt={'李宁':'一切皆有可能','耐克':'Just do it','阿迪达斯';'Impossible is nothing'}
SyntaxError: invalid syntax
>>> dirt={'李宁':'一切皆有可能','耐克':'Just do it','阿迪达斯':'Impossible is nothing'}
>>> print('李宁的口号是：',dirt['李宁'])
李宁的口号是： 一切皆有可能
>>> dirt[''李宁]
SyntaxError: invalid syntax
>>> dirt['李宁']
'一切皆有可能'
>>> dirt2{1:'one',2:'two',3:'three'}
SyntaxError: invalid syntax
>>> dirt2{1:'one',2:'two',3:'three'}
SyntaxError: invalid syntax
>>> dirt2={1:'one',2:'two',3:'three'}
>>> dirt2[2]
'two'
>>> dirt3={}
>>> dirt3
{}
>>> dict3=dict((('F',70,('i',105),('h',104),('C',67)))))
SyntaxError: invalid syntax
>>> dict3=dict((('F',70,('i',105),('h',104),('C',67))))
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    dict3=dict((('F',70,('i',105),('h',104),('C',67))))
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> dict3=dict((('F',70),('i',105),('h',104),('C',67))))
SyntaxError: invalid syntax
>>> dict3=dict((('F',70),('i',105),('h',104),('C',67)))
>>> 
>>> dic4
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    dic4
NameError: name 'dic4' is not defined
>>> dict3
{'C': 67, 'i': 105, 'F': 70, 'h': 104}
>>> dict4=dict(小甲鱼='让编程改变世界',苍井空='让AV征服所有宅男')
>>> dict4['苍井空']='所有AV从事者都要学习编程来提高职业技能'
>>> dict4
{'小甲鱼': '让编程改变世界', '苍井空': '所有AV从事者都要学习编程来提高职业技能'}
>>> dict4['爱迪生']='天才就是99%的汗水+1灵感，但这1%的灵感远远逼99%的汗水更重要'
>>> dict4
{'小甲鱼': '让编程改变世界', '苍井空': '所有AV从事者都要学习编程来提高职业技能', '爱迪生': '天才就是99%的汗水+1灵感，但这1%的灵感远远逼99%的汗水更重要'}
>>> 
>>> 
>>> 
>>> 还是字典
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    还是字典
NameError: name '还是字典' is not defined
>>> 
>>> 
>>> dict1={}
>>> dict1.fromkeys((1,2,3))
{1: None, 2: None, 3: None}
>>> dict1.fromkeys((1,2,3),'number')
{1: 'number', 2: 'number', 3: 'number'}
>>> dict1.fromkeys((1,2,3)),('one','two','three'))
SyntaxError: invalid syntax
>>> dict1.fromkeys((1,2,3),('one','two','three'))
{1: ('one', 'two', 'three'), 2: ('one', 'two', 'three'), 3: ('one', 'two', 'three')}
>>> dict1.fromkeys(1,3),'数字'）
SyntaxError: invalid character in identifier
>>> dict1.fromkeys(1,3),'数字')
SyntaxError: invalid syntax
>>> dict1.fromkeys((1,3),'数字')
{1: '数字', 3: '数字'}
>>> 
>>> #访问字典
>>> dict1=dict1.fromkeys(range(32)),'赞'）
SyntaxError: invalid character in identifier
>>> dict1=dict1.fromkeys(range(32)),'赞')
SyntaxError: invalid syntax
>>> dict1=dict1.fromkeys((range(32)),'赞')
>>> dict1
{0: '赞', 1: '赞', 2: '赞', 3: '赞', 4: '赞', 5: '赞', 6: '赞', 7: '赞', 8: '赞', 9: '赞', 10: '赞', 11: '赞', 12: '赞', 13: '赞', 14: '赞', 15: '赞', 16: '赞', 17: '赞', 18: '赞', 19: '赞', 20: '赞', 21: '赞', 22: '赞', 23: '赞', 24: '赞', 25: '赞', 26: '赞', 27: '赞', 28: '赞', 29: '赞', 30: '赞', 31: '赞'}
>>> 
>>> for eachkey in dict1.keys():
	print(eachkeys)

	
Traceback (most recent call last):
  File "<pyshell#51>", line 2, in <module>
    print(eachkeys)
NameError: name 'eachkeys' is not defined
>>> for eachKey in dict1.keys():
	print(eachKeys)

	
Traceback (most recent call last):
  File "<pyshell#53>", line 2, in <module>
    print(eachKeys)
NameError: name 'eachKeys' is not defined
>>> for eachKey in dict1.keys():
	print(eachKey)

	
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
>>> for eachvalue in dict1.values():
	print(eachvalue)

	
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
>>> for eachitem in dict1.values():
	print(eachitem)

	
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
>>> for eachitem in dict1.items():
	print(eachitem)

	
(0, '赞')
(1, '赞')
(2, '赞')
(3, '赞')
(4, '赞')
(5, '赞')
(6, '赞')
(7, '赞')
(8, '赞')
(9, '赞')
(10, '赞')
(11, '赞')
(12, '赞')
(13, '赞')
(14, '赞')
(15, '赞')
(16, '赞')
(17, '赞')
(18, '赞')
(19, '赞')
(20, '赞')
(21, '赞')
(22, '赞')
(23, '赞')
(24, '赞')
(25, '赞')
(26, '赞')
(27, '赞')
(28, '赞')
(29, '赞')
(30, '赞')
(31, '赞')
>>> print(dict1[31])
赞
>>> dict1.get(32)
>>> print(dict1.get(32))
None
>>> dict1.get(32,'木有')
'木有'
>>> dict1.get(32,'有')
'有'
>>> dict1.get(31,'木有')
'赞'
>>> dict1
{0: '赞', 1: '赞', 2: '赞', 3: '赞', 4: '赞', 5: '赞', 6: '赞', 7: '赞', 8: '赞', 9: '赞', 10: '赞', 11: '赞', 12: '赞', 13: '赞', 14: '赞', 15: '赞', 16: '赞', 17: '赞', 18: '赞', 19: '赞', 20: '赞', 21: '赞', 22: '赞', 23: '赞', 24: '赞', 25: '赞', 26: '赞', 27: '赞', 28: '赞', 29: '赞', 30: '赞', 31: '赞'}
>>> dict1.clear()
>>> dict1
{}
>>> dict1{}
SyntaxError: invalid syntax
>>> dict1={}
>>> a={'姓名'：'owen'}
SyntaxError: invalid character in identifier
>>> a={'姓名':'owen'}
>>> b=a
>>> b
{'姓名': 'owen'}
>>> a={}
>>> b
{'姓名': 'owen'}
>>> a
{}
>>> a.clear()
>>> b
{'姓名': 'owen'}
>>> a=b
>>> b.clear()
>>> b
{}
>>> a
{}
>>> #a={}，只是让a指向一个空集，但是字典还是存在内存里面，b还是指向它的
>>> #所以应该要clear()直接删除内存里面的东西
>>> 
>>> dir(dict)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> 
>>> a={1:'one',2:'two',3:'three'}
>>> b=a.copy()
>>> c
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    c
NameError: name 'c' is not defined
>>> c=a
>>> c
{1: 'one', 2: 'two', 3: 'three'}
>>> a
{1: 'one', 2: 'two', 3: 'three'}
>>> b
{1: 'one', 2: 'two', 3: 'three'}
>>> id(a)
61831968
>>> id(b)
61831688
>>> id(c)
61831968
>>> c[4]='four'
>>> c
{1: 'one', 2: 'two', 3: 'three', 4: 'four'}
>>> id(c)
61831968
>>> a
{1: 'one', 2: 'two', 3: 'three', 4: 'four'}
>>> b
{1: 'one', 2: 'two', 3: 'three'}
>>> 
>>> 
>>> a
{1: 'one', 2: 'two', 3: 'three', 4: 'four'}
>>> a.pop(2)
'two'
>>> a
{1: 'one', 3: 'three', 4: 'four'}
>>> a.popitem()
(1, 'one')
>>> 
>>> 
>>> a
{3: 'three', 4: 'four'}
>>> a.setdefault('小白')
>>> a
{3: 'three', 4: 'four', '小白': None}
>>> a.setdefault(5,'five')
'five'
>>> a
{3: 'three', 4: 'four', '小白': None, 5: 'five'}
>>> #字典里面没有顺序的概念~~
>>> 
>>> b={'小白'：'dog'}
SyntaxError: invalid character in identifier
>>> b={'小白':'dog'}
>>> a.update(b）
	 
SyntaxError: invalid character in identifier
>>> a.update(b)
>>> a
{3: 'three', 4: 'four', '小白': 'dog', 5: 'five'}
>>> b={'3':'我的幸运数字'}
>>> a.update(b)
>>> 
>>> a
{3: 'three', 4: 'four', '小白': 'dog', '3': '我的幸运数字', 5: 'five'}
>>> # 上面那个是赋值的update
>>> 
>>> 
>>> 
>>> 
>>> #在我的世界里你就是唯一
>>> num ={}
>>> type(num)
<class 'dict'>
>>> num2={1.2,3,4,5}
>>> type(num2)
<class 'set'>
>>> 
>>> #只是一个集合
>>> 
>>> num2={1,2,3,4,5,5,4,3,2,1}
>>> num2
{1, 2, 3, 4, 5}
>>> num2[2]
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    num2[2]
TypeError: 'set' object does not support indexing
>>> #集合不支持索引，虽然它会自动删除重复的元素
>>> set1=set([1,2,3,4,5])
>>> set1
{1, 2, 3, 4, 5}
>>> 
>>> num1=[1,2,3,4,5,5,3,1,0]
>>> temp=[]
>>> for each in num1:
	if each not in temp:
		temp.append(each)

		
>>> temp
[1, 2, 3, 4, 5, 0]
>>> num1
[1, 2, 3, 4, 5, 5, 3, 1, 0]
>>> temp=list(set(temp))
>>> temp
[0, 1, 2, 3, 4, 5]
>>> num1=list(set(num1))
>>> num1
[0, 1, 2, 3, 4, 5]
>>> num2=[1,2,3,4,5,2,1,0]
>>> num2=(set(num2))
>>> num2
{0, 1, 2, 3, 4, 5}
>>> num2=[4,9,6,5,2,1,0]
>>> num2=(set(num2))
>>> num2
{0, 1, 2, 4, 5, 6, 9}
>>> 
>>> 1 in num2
True
>>> '1' in num2
False
>>> num2
{0, 1, 2, 4, 5, 6, 9}
>>> num2.add(6)
>>> num2
{0, 1, 2, 4, 5, 6, 9}
>>> num2.remove(5)
>>> num2
{0, 1, 2, 4, 6, 9}
>>> 
>>> #不可变集合
>>> 
>>> frozenset()
frozenset()
>>> num3=frozenset()
>>> num3.add(3)
Traceback (most recent call last):
  File "<pyshell#182>", line 1, in <module>
    num3.add(3)
AttributeError: 'frozenset' object has no attribute 'add'
>>> 
>>> 
>>> 
>>> 
>>> #文件之 ，因为懂你所以永恒
>>> 
>>> 
