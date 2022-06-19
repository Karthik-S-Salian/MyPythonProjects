
"""
index: 0, 1, 2, 3, ......
or
......, -3, -2, -1
"""

# SORT
list2 = [1, 2, 3, 4, 5]
list2.sort()  # sorts in ascending order
list1 = sorted(list2)  # returns copy of list in sorted order dont sort original


# 1 List with same items
list4 = [0] * 5

# 2   CONCATINATE TWO LIST
list3 = list1 + list2
print(list3)

#  3.  SLICING THE LIST
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = list1[1:4]  # last index is excluded
print(list2)

print(list1[:4])  # = 1,2,3,4,5
print(list1[6:])  # = 6,7,8

print(list1[::1])  # = 1,2,3,4,5,6,7,8,9
print(list1[::2])  # = 1,3,5,7,9
print(list1[::-1])  # = 9,8,7,6,5,4,3,2,1

# 4. COPYING THE LIST
list_original = [1, 3, 5, 7]
list_cpy = list_original  # = 1,3,5,7     NOT PERFECT

# CORRECT WAY
list_copy = list_original.copy()
list_copy = list(list_original)
list_copy = list_original[:]

# 5. LIST COMPERHENSION
a = [1, 2, 3, 4, 5]
b = [i for i in a]

list_name = [i ** 2 for i in a]  # a=list or any iterable

# 6.
print(list1.count(1))  # count no of times item repeated
#

# TUPLE

tuple3=(9,)      # must have comma at the end if not it is recognised as common variable
print(tuple3)

l=[1,2,3,4,5]
# TYPE CONVERSION TUPLE
tuple3=tuple(l)

"""
indexing 0,1,2.....
        or
        .....,-3,-2,-1
"""

def asterisk():

    ones=[1]*5  # create list with 5 elments of 1
    zeros=(0)*5   # create tuple with 5 elments of 0

    list1=[0,1]*10  # repeats elements contains double of 10

    word="AB"*10

    print(ones,zeros,list1,word,sep="\n")