print(111)

list1=[11,33,44]

list1.pop(2)
print(list1)

list2=[67,994,"1",[1,3],[1,3]]
print(list2.count([1,3]),"[1,3]")

list1.extend(list2)
list1.reverse()
print(list1)


tuple1=(4,)
print(tuple1)

dict1={"key1":1,"key2":2,"key3":3}
dict1.popitem()
print(dict1)

set1=set([1,2,3,4,5])
set2=set([2,3,4])
print(set1&set2)#交集
print(set1|set2)#并集


join="_"
name="abcde"
print(name*3)
joinResult=join.join(name)
print(joinResult)
print(joinResult.split("_"))


