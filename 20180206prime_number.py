# -*- coding: UTF-8 -*-
 
''''' 
求质数或素数 
先弄清楚什么是质数？ 
质数就是只能被1和它本身整除的数，1和0不是质数也不是合数 
'''  
  
def primeNumber(n):  
    x = 1    # x累计1到n中的质数个数，由于2也是质数，这里先加+1  
    for i in range(3,n+1):  # 3到n+1取值（取一个值出来用内循环判断此数是否为质素）  
        result = True  
        for j in range(2,i-1):   # 2到i-1之间有没有被整数的数，有则不是质素  
            if i % j == 0:  
                result = False  
        if result == True:  
            print i,  
            x += 1  
    print '\n%d 内有 %d 个质数' %(n,x)  
primeNumber(1000)  