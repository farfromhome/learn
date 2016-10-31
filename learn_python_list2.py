>>> 
>>> #一般元组用小括号，列表用中括号
>>> tuple1 =(1,2,3,4,5,6,7,8)
>>> tuple1
(1, 2, 3, 4, 5, 6, 7, 8)
>>> tupel(1)
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    tupel(1)
NameError: name 'tupel' is not defined
>>> tuplel(1)
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    tuplel(1)
NameError: name 'tuplel' is not defined
>>> tuple1(1)
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    tuple1(1)
TypeError: 'tuple' object is not callable
>>> tuple1
(1, 2, 3, 4, 5, 6, 7, 8)
>>> tuple1(1)
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    tuple1(1)
TypeError: 'tuple' object is not callable
>>> tuple1[1]
2
>>> tuple1[5:]
(6, 7, 8)
>>> tuple1[:5]
(1, 2, 3, 4, 5)
>>> tuple2=tuple1[:]
>>> tuple2
(1, 2, 3, 4, 5, 6, 7, 8)
>>> 
>>> tuple1[1]=3
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    tuple1[1]=3
TypeError: 'tuple' object does not support item assignment
>>> temp = (1)
>>> temp
1
>>> type(temp)
<class 'int'>
>>> temp2 = 1,2,3,4,5
>>> type(temp2)
<class 'tuple'>
>>> temp[]
SyntaxError: invalid syntax
>>> temp[ ]
SyntaxError: invalid syntax
>>> temp=[]
>>> type(temp)
<class 'list'>
>>> temp=()
>>> type(temp)
<class 'tuple'>
>>> temp=(1,)
>>> type(temp)
<class 'tuple'>
>>> temp=1,
>>> type(temp)
<class 'tuple'>
>>> 8*(8)
64
>>> 8*(8,)
(8, 8, 8, 8, 8, 8, 8, 8)
>>> 
>>> 
>>> 
>>> temp=('小甲鱼'，'黑夜','迷途'，'小布丁')
SyntaxError: invalid character in identifier
>>> temp=('小甲鱼','黑夜','迷途','小布丁')
>>> temp= temp[0:2] +('黑夜'，)+ temp[2:]
SyntaxError: invalid character in identifier
>>> temp= temp[0:2] +('黑夜',)+ temp[2:]
>>> temp
('小甲鱼', '黑夜', '黑夜', '迷途', '小布丁')
>>> temp= temp[0:2] +('意境',)+ temp[2:]
>>> temp
('小甲鱼', '黑夜', '意境', '黑夜', '迷途', '小布丁')
>>> 
>>> 
>>> del temp
>>> temp
Traceback (most recent call last):
  File "<pyshell#197>", line 1, in <module>
    temp
NameError: name 'temp' is not defined





>>> #字符串
>>> str1 = 'I am a handsome boy'
>>> str6[:6]
Traceback (most recent call last):
  File "<pyshell#206>", line 1, in <module>
    str6[:6]
NameError: name 'str6' is not defined
>>> str[:6]
Traceback (most recent call last):
  File "<pyshell#207>", line 1, in <module>
    str[:6]
TypeError: 'type' object is not subscriptable
>>> str1[:6]
'I am a'
>>> str1
'I am a handsome boy'
>>> 
>>> str1[:6] + '插入字符串'+str1[6:]
'I am a插入字符串 handsome boy'
>>> str1
'I am a handsome boy'
>>> str1=  str1[:6] + '插入字符串'+str1[6:]
>>> str1
'I am a插入字符串 handsome boy'
>>> str2 = 'xiaoxie'
>>> str2.capitalize()
'Xiaoxie'
>>> str2.casefold()
'xiaoxie'
>>> str2.center(width)
Traceback (most recent call last):
  File "<pyshell#218>", line 1, in <module>
    str2.center(width)
NameError: name 'width' is not defined
>>> str2.center(18)
'     xiaoxie      '

