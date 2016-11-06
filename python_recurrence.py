def factional(n):
    if n==1:
        return 1
    else:
        return n*factional(n-1)

number=int(input('please input a int number'))
result=factional(number)
print('%d 的阶乘是：%d' %(number,result))
