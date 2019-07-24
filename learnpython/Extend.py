class Parent():
    x=100
    def __init__(self):
        print("parent init")
    def sayHello(self):
        print("parent hello")

class Child(Parent):
    x=200
    def __init__(self):
        Parent.__init__(self)
        print("child init")
    def sayHello(self):
        print("child hello")

var1 =Child()
print(var1.x)
var1.sayHello()