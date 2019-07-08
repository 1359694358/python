import os
'''
回顾：注释，输入和输出，标识符，保留字，字符串，数字，// ,/ %
    切片
今日：
'''
# str1='hello'
# print(str1.upper())         #将字符串大写
# print(str1.capitalize())    #将首字母大写
# print(str1.lower())         #将字符串小写

''''''
'''假设一个字符串的长度为单数,将最中间的那个字符大写
比如：hello  heLlo     5//2 =2
      welcome welCome  7//2 =3
      9//2=4
'''
# name='welcomethyj'
# length=len(name)//2  #求这个字符串的长度
# re=name[:length]+name[length:length+1].upper()+name[length+1:]
# print(re)


'''
 join:以指定的字符连接字符串，
       os.path.join()
 split: 拆分一个字符串，
'''
# str1='hello'
# print('-'.join(str1))
# path=os.path.join('/user/','destdop/','python')
# print(path)
'''

'''
# str1='welcome[15212412]denglu'
# newstr=str1.split('[')[1].split(']')[0]
# print(newstr)


'''布尔值：True,False
    任何非0： 0
    非空：None  
    长度非0:
    的东西是真 ,bool方法返回 
'''
# a=[1]
# print(bool(a))


'''
逻辑运算符
and  x and y  如果x为false,返回X,如果x为True，返回的是Y
or   x or Y   如果x为真，返回X，如果x为假，返回Y
not
'''

# x=1
# y=0
# z=x or y
# print("z的值是什么：{}".format(z))
# print("z的布尔类型是:{}".format(bool(z)))
# print(not y)

'''
in  not in 
'''
# str1='hello'
#
# print('h' not in str1)

'''is 
   is not
'''
# a,b=3,5
# print("a的内存地址：{1}，b的内存地址是：{0}".format(id(b),id(a)))
# print(a is not b)

'''
数组:list,用[]表示：一种有序的集合，可以随时添加和删除其中的元素
索引;从0开始
长度：len(list)
type:查看类型,isinstance:返回数据类型的布尔值
最后一个元素的索引：length-1
list里面的元素可以是不同的数据类型
列表也可以切片，和字符串切片一样的
'''
# print(isinstance(list1,str))
# print('list1的类型是：{},它的长度是：{}，它的第二个元素是：{}'.format(type(list1),len(list1),list1[2]))
# print(type(list1[len(list1)-1]))
# print('list1的最后一个元素里面的第三个元素是：{}'.format(list1[4][2]))
list1=['tom','jack',8,3.14159,[1,2,3]]
# str1='abc'
# list2=['a','b','c']
#print(list1.clear())   #清除列表里面所有的元素
#print(list1.reverse())  #颠倒顺序
# list1.append('fei')   #增加一个元素，默认加在列表最后
# list1.insert(3,'hao') #增加指定位置的元素
# list1.extend(list2)   #把一个序列里面的内容添加到列表中
#list1.remove(8)       #删除指定的元素
#list1.pop(1)           #删除指定索引的元素
#list3=list1.copy()      #复制列表
#print("list1修改之后为:{}".format(list3))
#print(list1[2:4])

'''元组：用括号表示，和列表类型，不同之处元素不能修改

'''
tp=(1,2,['a','b','c'])
print('tp第二个元素,修改之前的地址',id(tp[2]))
tp[2].append('d')
print('tp第二个元素，修改之后的地址',id(tp[2]))


'''字典，set
'''


