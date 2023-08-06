class MatematikaN:

    def __init__(self):
        print()

    def show(self,name): 
        print("Hello",name)


# 1 функция факториал
    def factorial(self,n):
        factorial = 1
        while n > 1:
            factorial *= n
            n -= 1
        return print(factorial)

class Student: 
    # Constructor - non parameterized 
    def __init__(self): 
        print("This is non parametrized constructor") 
    def show(self,name): 
        print("Hello",name)
