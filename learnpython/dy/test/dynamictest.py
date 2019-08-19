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
result=getattr(dm,"fuck")
print(result)

dm.fuck()