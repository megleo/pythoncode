# -*- codeing = utf-8 -*-
# @Auther : menglei 2021180020
# @Filer : 1.py.py
# @Software : PyCharm
# @Time ： 2021/9/28 8:20 下午

#  变量定义方式
a = 10
b = 20
print(a,b)

c,d = 30,40
print(c,d)

# 两个数值之间进行交换的方式

'''
普通方式
'''
e = a
a = b
b =e
print(a,b)
'''
利用python定义变量的语法来实现
'''

c,d = d,c
print(c,d)