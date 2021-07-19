def Outer_Function(x):
    def Inner_Function(y):
        print(x)
        print(y)
    return Inner_Function
Result = Outer_Function(100)
Result(50)
