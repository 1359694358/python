

count=0

while count<10:
    count += 1
    if count%2==0:
        continue
    if count>=8:
        break
    print("count:{}".format(count))


for index in range(10,20):
    print(index)

dic={"id":1,"name":"fuck"}
for key in  dic:
    print("key:{}".format(key))