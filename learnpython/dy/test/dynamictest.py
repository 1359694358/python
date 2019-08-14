class DynamicClass:
    def hello(self):
        print("hello")
        pass

    pass


def fuck():
    print("fuck")
    pass

dm=DynamicClass()
setattr(dm,"fuck",fuck)
result=getattr(DynamicClass,"fuck")
print(result)

dm.fuck()