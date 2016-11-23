Type "copyright", "credits" or "license()" for more information.
>>> a=[i for i in range (100)]if not (i%2) and i%3]
SyntaxError: invalid syntax
>>> a=[i for i in range (100)if not (i%2) and i%3]
>>> a
[2, 4, 8, 10, 14, 16, 20, 22, 26, 28, 32, 34, 38, 40, 44, 46, 50, 52, 56, 58, 62, 64, 68, 70, 74, 76, 80, 82, 86, 88, 92, 94, 98]
>>> b={i:i % 2 ==0 for i in range (10)}
>>> b
{0: True, 1: False, 2: True, 3: False, 4: True, 5: False, 6: True, 7: False, 8: True, 9: False}
>>> c={i for i in [1,2,3,4,5,2,3,5,6,7,8,2]}
>>> c
{1, 2, 3, 4, 5, 6, 7, 8}
>>> e=(i for i in range(10))
>>> e
<generator object <genexpr> at 0x03DBBCC0>
>>> next(e)
0
>>> next(e)
1
>>> for each in e:
	print(each)

	
2
3
4
5
6
7
8
9
>>> sum(i for i in range(10)if i % 2)
25
>>> sum(i for i in range(5)if i % 2)
4
>>> 
