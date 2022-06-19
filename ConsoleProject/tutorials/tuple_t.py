

#        TUPLE

# TUPLES ARE CONSTANT CANNOT CHANGE VALUE AFTER ONCE ASSIGNED

tuple1=(1,2)
print(tuple1)

tuple2=tuple()
print(tuple2)

#VI // for one item tuple
tuple3=(9,)      # must have comma at the end if not it is recognised as common variable
print(tuple3)

l=[1,2,3,4,5]
# TYPE CONVERSION TUPLE
tuple3=tuple(l)  #         x=list or any iterable

"""
indexing 0,1,2.....
        or
        .....,-3,-2,-1
"""


# UNPACK ELEMENTS
tuple2=("john",12,"peru")
name,age,city = tuple2
print(name,age,city)

# unpacking multiple value for one variable

tuple1=[1,2,3,4,5]
i1, *i2 ,i3 = tuple1
print(i1)
print(i2)   # 2,3,4   converted into list
print(i3)

