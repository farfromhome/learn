//删除数组的元素
方法一
>>> group=['xixo','oxoxo','ososos','eieiei']
>>> group.pop()
'eieiei'
>>> group
['xixo', 'oxoxo', 'ososos']
>>> name=group.pop()
>>> group
['xixo', 'oxoxo']
>>> 

方法二
>>> member
['牡丹', '小甲鱼', '小布丁', '迷恋大叔', '意境', '竹林小溪', '成功', '成功']
>>> member.remove('小布丁')
>>> member
['牡丹', '小甲鱼', '迷恋大叔', '意境', '竹林小溪', '成功', '成功']

方法三
>>> del member[1]
>>> member
['牡丹', '迷恋大叔', '意境', '竹林小溪', '成功', '成功']
>>> del group
>>> group
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    group
NameError: name 'group' is not defined

>>> member[1:3]
['迷恋大叔', '意境']
>>>  member
>>> member
['牡丹', '迷恋大叔', '意境', '竹林小溪', '成功', '成功']
>>> member[:3]
['牡丹', '迷恋大叔', '意境']
>>> member[:]
['牡丹', '迷恋大叔', '意境', '竹林小溪', '成功', '成功']
>>> member2=member[:]
>>> member
['牡丹', '迷恋大叔', '意境', '竹林小溪', '成功', '成功']





// 在数组中加入元素
>>> member=['小甲鱼','小布丁','迷恋大叔','意境']
>>> member.append('竹林小溪')
>>> menber
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    menber
NameError: name 'menber' is not defined
>>> member
['小甲鱼', '小布丁', '迷恋大叔', '意境', '竹林小溪']
>>> member.extend(['成功','成功'])
>>> member
['小甲鱼', '小布丁', '迷恋大叔', '意境', '竹林小溪', '成功', '成功']
>>> member.insert(0,'牡丹')
>>> member
['牡丹', '小甲鱼', '小布丁', '迷恋大叔', '意境', '竹林小溪', '成功', '成功']
>>> 
  

 
 
 列表
 >>> list1=[123]
>>> list2=[234]
>>> list1>list2
False
>>> list1=[123,456]
>>> list2=[234,123]
>>> list1>list2
False
>>> list3=[123,456]
>>> (list1<list2) and (list1 == list3)
True
>>> list4 =list1 + list2
>>> list3
[123, 456]
>>> list4
[123, 456, 234, 123]


>>> list1
[123, 456]
>>> list1.extend('小甲鱼')
>>> list1
[123, 456, '小', '甲', '鱼']
 
>>> list1.insert(1,'owen')
>>> list1
[123, 'owen', 456, '小', '甲', '鱼'] 

>>> list1.insert(2,'nanxy')
>>> list1
[123, 'owen', 'nanxy', 456, '小', '甲', '鱼']
>>> list1.insert(2,'小甲鱼')
>>> list1
[123, 'owen', '小甲鱼', 'nanxy', 456, '小', '甲', '鱼']
>>> list1.extend('owen)
>>> list1
[123, 'owen', '小甲鱼', 'nanxy', 456, '小', '甲', '鱼', 'o', 'w', 'e', 'n']  
                 
 list3
[123, 456]
>>> list3*3
[123, 456, 123, 456, 123, 456]
>>> 123 in list3
True 
>>> 'owen' not in list3
True  

>>> list5 =[123,['小甲鱼','牡丹'],456]
>>> '小甲鱼' in list5
False
>>> '小甲鱼' in list5[1]
True
>>> list5[1][1]
'牡丹'
                 
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> list3
[123, 456]
>>> list3.count(123)
1
>>> 
>>> 
>>> list3.index(123)
0
>>> 
>>> 
>>> list1
[123, 'owen', '小甲鱼', 'nanxy', 456, '小', '甲', '鱼', 'o', 'w', 'e', 'n']
>>> list1.reverse
<built-in method reverse of list object at 0x03182558>
>>> list1.reverse()
>>> list1
['n', 'e', 'w', 'o', '鱼', '甲', '小', 456, 'nanxy', '小甲鱼', 'owen', 123]
>>> list6 = [4,2,4,1,5,6,23,32,0]
>>> list.sort()                 
                 
                 
>>> list6.sort()
>>> list6
[0, 1, 2, 4, 4, 5, 6, 23, 32]
>>> list6.sort(reverse=True)
>>> list6
[32, 23, 6, 5, 4, 4, 2, 1, 0]
>>> 
>>> 
>>> list7=list6[:]
>>> list7
[32, 23, 6, 5, 4, 4, 2, 1, 0]
>>> 
>>>                  
>>> list8=list6
>>> list8
[32, 23, 6, 5, 4, 4, 2, 1, 0]
>>> list6.sort()
>>> list6
[0, 1, 2, 4, 4, 5, 6, 23, 32]
>>> list7
[32, 23, 6, 5, 4, 4, 2, 1, 0]
>>> list8
[0, 1, 2, 4, 4, 5, 6, 23, 32]
>>> #  =是一直赋值                 
