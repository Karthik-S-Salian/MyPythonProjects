import functools


def fun6(name):
    return f"hello {name}"""

def fun7(name):
    return f"hello {name}, how are you?"

def fun8(fun9):    # PASSING FUNCTION AS ARGUMENT
    return fun9("sujal")

def fun():
    print("first function")
    def fun1():
        print("first child function")
    def fun2():
        print("second child function")
    fun2()
    fun1()

def fun11():
    def fun1():
        return "hello "
    return fun1()       #RETURNING FUNCTION


def decorator1():
    def fun12(fun13):
        def wrapper():
            print("hello")
            fun13()
            print("world")

        return wrapper

    def fun14():
        print("python")

    fun14 = fun12(fun14)
    fun14()

def decorator2():
    def fun12(fun13):
        def wrapper():
            print("hello")
            fun13()
            print("world")

        return wrapper

    @fun12
    def fun14():
        print("python")

    fun14()

def decorator3():
    def fun15(fun16):
        def wrapper(*args):
            print("hello")
            fun16(*args)
            print(" world")

        return wrapper

    @fun15
    def fun16(name):
        print(f'{name}')

    fun16("python")





# FANCY DECORATOR

# CLASS DECORATOR

def class_decorator():
    class  Square:
        def __init__(self,side):
            self._side=side

        @property

        def side(self):
            return self._side

        @side.setter
        def side(self,value):
            if value>=0:
                self._side=value
            else:
                print("error")
        @property
        def area(self):
            return self.side**2

        @classmethod
        def unit_square(cls):
            return cls(1)

    s=Square(5)

    print(s.side)
    print(s.area)


def singleton_class():
    def singleton(classs):
        @functools.wraps(classs)
        def wrapper(*args, **kwargs):
            if not wrapper.instance:
                wrapper.instance = classs(*args, **kwargs)
            return wrapper.instance

        wrapper.instance = None
        return wrapper

    @singleton
    class one:
        pass

    first=one()
    second=one()

    print(first is second)

def arg_decorator():
    def repeat(num):
        def decorator_repeat(fun21):
            @functools.wraps(fun21)
            def wrapper(*args,**kwargs):
                value=None
                for _ in range(num):
                    value=fun21(*args,**kwargs)
                return value
            return wrapper
        return decorator_repeat

    @repeat(num=5)
    def fun21(name):
        print(f"{name}")

    fun21("python")


if __name__=="__main__":
    print(fun8(fun6))
    print(fun8(fun7), "\n")
    fun()
    fun11()

    print("\n decorator 1")
    decorator1()
    print("\n decorator 2")
    decorator2()
    print("\n decorator 3 ")
    decorator3()
    print("\n class decorator ")
    class_decorator()

    print('\n singleton class ')
    singleton_class()

    print('\n decorator with arguments ')
    arg_decorator()








