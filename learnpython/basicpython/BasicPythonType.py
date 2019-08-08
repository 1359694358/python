array=[1,2,3,3,4,5,6,8,3,3]

for index in range(array.count(3)):
    array.remove(3)
print(array)

array=[1,2,3,3,4,5,6,8,3,3]
while array.count(3)>0:
    array.remove(3)
print(array)