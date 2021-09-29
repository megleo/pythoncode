# -*- codeing = utf-8 -*-
# @Auther : menglei 2021180020
# @Filer : dict.py
# @Software : PyCharm
# @Time ： 2021/9/29 8:06 上午
'''
+ 字典也是用来存储一组或者多组数据的时候使用
+ 使用大括号{}
+ 字典是键值对的存储方式 name ：admin
+ 键值之间通过冒号进行分割，多组键值对之间使用逗号进行分割
+ 键必须是字符串或者数字，值可以是任意类型
'''
# 一本书的相关数据 数名，作者， 价格， 。。。
vard = {'title':'<<鬼谷子>>', 'author':'鬼谷子','price':29.99}
print(vard,type(vard))

# 获取键的值

print(vard['title'])
print(vard['price'],type(vard['price']))