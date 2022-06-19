from math import floor
from functools import reduce


# LAMBDA FUNCTIONS ,MAP ,FILTER , REDUCE , GENERATORS

def  fun():
    def hai(a,b,c,d=9):
        print(a,b,c,d)
    #POSITIONAL ARGUMENT
    hai(1,2,3)

    #KEYWORD ARGUMENT
    hai(a=1,c=4,b=2,d=0)


    #  * -> can take any number of positional arguments  ->tuple
    # ** -> take any number of keyword arguments  -> dictionary
    def fun31(a,b,*args,**kwargs):
        print("a & b = ",a,b,end="\n")

        for x in args:
            print(x,end=" ")
        print("")
        for key in kwargs:
            print(key," = ",kwargs[key],end=" ")

    fun31(1,2,3,4,5,6,s=7,i=10,j='hai')


    def fun32(a,b,*,c,d):   # every element after * or * args must be keyword arguments
        print(a,b,c,d)

    fun32(1,2,c=3,d=4)

    # unpacking list or tuple to a function
    def fun33(a,b,c):
        print(a,b,c)

    list2=[1,2,3]
    fun33(*list2)   # unpacking list  // length of parameter = no of item in list

    dic1={"a":1,"b":2,"c":3}
    fun33(**dic1)    # keys = parameter name in function

    # SCOPE
    print("SCOPE")
    num=10
    def fun34(num):
        num=0
        print(num)
    fun34(num)             # immutable objects cannot be changed inside method
    print(num)

    list3=[1,12,4,5,8,5]
    def fun34(a_list):
        list3.append(2)
        a_list.append(45)
        list2=[1,2,3]
        a_list+=list2
        a_list=a_list+list2   # not same as above here create new list with local scope

        print(num)
    fun34(list3)             # mutable objects can be changed inside method
    print(list3)








def create_lamda():
    # lambda arguments: expressions
    # nameless functions
    x = lambda a: a * a
    print(x(3))

    # lambda functions are best used within other higher order functions
    def A(x):
        return (lambda y: x + y)

    t = A(4)
    print(t(8))


def lambda_with_filter():
    list1 = [1, 2, 3, 4, 6, 8, 9, 10, 11, 12]

    # filter(function,iterables)    //function = condition
    # filter returns object node therefore passed to list
    newlist = list(filter(lambda a: (floor(a / 3) == a / 3), list1))
    print(newlist)


def lambda_with_map():
    list1 = [1, 2, 3, 4, 6, 8, 9, 10, 11, 12, 13, 15]
    list2 = list(range(10))

    # map(function,iterables)

    print(list(map(lambda a: (a / 3 != 2), list1)))

    print(list(map(lambda a: (a * a), list1)))

    def add(a, b):
        return a + b

    print(list(map(add, list1, list2)))  # output list has element as element in small list


def lambda_with_reduce():
    list1 = [1, 2, 3, 4, 6, 8, 9, 10, 11, 12]

    # reduce(function,sequence)

    print(reduce(lambda a, b: (a + b), list1))


def linear_equations():
    s = lambda a: a * a + 3 * a + 2
    print(s(4))

    c = lambda a, b: a + b
    print(c(3, 4))

############################################################################################################
#-------------------------------------------GENERATORS-----------------------------------------------------#
def ex1():
    def ex_generator():
        yield 'hello'
        yield 'world'

    itr=ex_generator()   # making a object (here itr ) is must
    print(next(itr))
    print(next(itr))

def ex2():
    def fibbonacci_seq():
        a,b=0,1
        while True:
            yield a
            a,b=b,a+b

    for f in fibbonacci_seq():
        if f>50:
            break
        print(f)


if __name__ == "__main__":
    fun()
    print("\n lambda function")
    #create_lamda()
    print("\n FILTER")
    #lambda_with_filter()
    print("\n  MAP")
    #lambda_with_map()
    print("\n  REDUCE")
    #lambda_with_reduce()
    print("\n")
    #linear_equations()
    print("\n")

    print("GENERATOR\n")
    ex1()
    print('\n fibbonacci sequence')
    ex2()

