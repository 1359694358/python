

count=0

while count<10:
    count += 1
    if count%2==0:
        continue
    if count>=8:
        break
    print("count:{}".format(count))

iterator=[1,43,78,4]
for item in iterator:
    print("item:{}".format(item),end=",")

print("")

for index in range(10,20,2):
    print(index)

dic={"id":1,"name":"fuck"}

for key in  dic:
    for idx in key:# loop get item char
        print(idx)
for key in  dic:
    print("key:{}".format(key))

sum=0
curI=1

while curI<=100:
    sum+=curI
    curI+=1
print(sum)


def sum(max):
    return int(max*(max+1)/2)
print(sum(100))


sortList=[1,57,1323,6,2]
sortList.sort()
print(sortList)

def pow(x,y):
    start=1
    resul=x
    while start<y:
        resul*=x
        start+=1
    return resul
print(pow(2,10))