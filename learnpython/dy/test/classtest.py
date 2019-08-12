class A():
    # def __init__(self,arg):
    #     print(arg)
    _testMethodName = ...  # type: str

    def __init__(self) -> None:
        ...
        print("111")

class B(A):
    def __init__(self,arg,fk):
        A.__init__(self)
        print(fk)


ins=B(1,2)
