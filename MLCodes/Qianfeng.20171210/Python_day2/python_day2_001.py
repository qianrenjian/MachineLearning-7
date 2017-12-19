#!/usr/bin/python
#-*- coding:utf-8 -*-
import string
import re
'''
一、基础类                        二、原生的数组                三、字符串的操作
1.1 工程方向                      2.1 元祖tuple		        3.1 字符串的转换
1.2 缩进                         2.2 列表 list		        3.2 字符串的长度
1.3 运算符		   	            2.3 字典 dict	            3.3 整合，进制
1.4 逻辑判断（与、或、非）	  2.4 循环 for ...in...              3.4 enumerrate()获取序列
1.5 赋值						                                3.5 type()+isinstance（对象，类型）获得对象类型
1.6 拼接操作 一						                        3.6 删除操作del
1.7 取值 二

四、基础数学运算                     五、导入模块                    六、对象比较
4.1 is && ==区别		             5.1 string模块		              6.1 支持多个比较操作
4.2 cmp（）比较 -1,0，1 	         5.2 re模块		  	              6.2 多个比较支持操作
4.3 round()四舍五入					                              6.3 in 操作、open操作
'''
# 1.1 工程方向
# def test():
#     print('Today is cool')
# 1.2 缩进
if __name__ == '__main__':
    # test()
    # 1.3 逻辑符判断
    # print 2 != 3
    # print 2 == 3
    # print 4 <> 5
#     1.4 and&&or区别
#     print(True and False)
#     print(True or False)

#     1.5 赋值

    # def test():
    #     # count = 3
    #     # count = count +1
    #     # count += 1
    #     # count *=3
    #     # print(count)
    #     # x = y = z = 1
    #     # print x , y , z
    #     x , y , z = 123 , 3.14 , 'I am a boy'
    #     x , z = z , x
    # #     交换
    #     print x , z
    # test()

    #1.6 字符串的操作
    # pystr = 'PYTHON'
    # iscool = 'IS COOL'
    # print pystr+'\t'+iscool
    # print( pystr* 4)

#    2.0 元祖

    # aTuple = ('Rose' , 123 , 3.13 ,'JACK')
    # print aTuple[:2]
    # print aTuple[-1]
    # print aTuple[1:3]
    # print type(aTuple)

#     2.1 列表
#     aList = [1,2,3,4,'a string']
#     print aList[0:2]
#     print aList[0:4]
#     print aList[-1]
#     print aList[::-3]
#  2.2 字典
#     aDict = {'name':'zhangsan'}
#     aDict['score'] = 100
#     print aDict,type(aDict)
#     print aDict.keys()
#     print aDict.values()
#     print aDict['score']
#     for key in aDict:
#         print key , aDict[key]

#     3.0 字符串之间的转换

    # x = int('666')
    # print x
    # y = str(777)
    # print y

#     3.1 字符串长度的方法
#     foo = 'abc'
#     print len(foo)
#     print range(len(foo))
#     print range(1,10,2)

# 3.2 enumerate函数用于遍历序列中的元素以及它们的下标

    # aDict = {'name':"zhangsan"}
    # aDict['score'] = 100
    # for(i , key) in enumerate(aDict):
    #     print i , key , aDict[key]
#  3.3 del
#     aList = [1,2,3,4]
#     del aList[-1]
#     print aList
#     print type(aList)

# 4.0 is 和 is not

#     foo1 = 3.4 ; foo2 = foo1
# #     foo1 == foo2 ==3.4
#     print foo1 == foo2
#     print foo1 is foo2

    # foo1 = 3.14
    # foo2 = 3 + 0.14
    # print foo1 == foo2
    # print foo1 is not foo2

#     4.1 cmp比较-1 ， 0 ，1
#     print cmp(4,5)
#     print cmp(4,4)
#     print cmp(4,2)

#    4.2 round四舍五入
#     print round(1000.4555)
#     print round(1000.121)
#     print round(1000.566)

    # print string.capitalize('today')
    # # 首字母大写
    # print string.lowercase
    # a-z 输出
    # print 'HELLO'.lower()
    # print string.split('ajjlj ljlj')
    # print string.lstrip('jjjjfsj   ')
    # print string.rsplit('    jjljljal')
    # print string.rstrip('   jjjss  ')

    # m = re.match('^ab+','abjsjjljsjg')
    # # search ,match
    # print m
    # print m.group()
    # a = re.match('c','cjklsjkj')
    # print a

#6.0 多个比较支持多个操作
    # print 3<5<7
    # # 3<5 and 5<7
    # print 4>3==3
    # print 2<4<8!=2<4

# 6.1 多个比较支持多个操作
#     print 'bc' in 'abcd'
#     print 'n' in 'ajlkj'
#     print 'nm' not in 'ajkja'


# 6.3 函数参数传递
#     def mytest(num):
#         return num * 5
#     def convert(func , aList):
#         print '集合里的元素都转换成同一个新的元素'
#         return [func(eachNum) for eachNum in aList]
#     Mylist = [123 ,1.12 ,-2e33 , 99999L]
#     print convert(int , Mylist)
#     print convert(long , Mylist)
#     print convert(float , Mylist)
#     print convert(mytest , Mylist)