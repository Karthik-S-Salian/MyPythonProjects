"""
#      LISTS

"""
list1 = list()  # CREATES  EMPTY LIST
list2 = []
list3 = [5, True, "hello", "hello"]  # CAN HOLD ANY TYPE

print(list3[0])
print(list3[-2])
"""
index: 0, 1, 2, 3, ......
or
......, -3, -2, -1
"""

#  ACCESSING ELEMENTS USING FOR LOOP
for i in list3:
    print(i)

# CHECKING FOR ELEMENTS
if "car" in list3:
    print("yes")
else:
    print("no")

# No OF ITEMS IN LIST
L = len(list1)

#  ADD  NEW  ITEM
list1.append("lorry")  # adds new item at end of list

list3.insert(2, "car")  # inserts at specific position

# DELETING ITEMS IN LIST

list2 = [1, 2, 3, 4, 5]

list2.pop()  # deletes  and returns last item

list2.remove(4)  # removes specific item

del list2[0]  # deletes element at specific position

list2.clear()  # deletes all the items

# SORT
list2 = [1, 2, 3, 4, 5]
list2.sort()  # sorts in ascending order

list1 = sorted(list2)  # returns copy of list in sorted order dont sort original

# REVERSE
list2.reverse()

# TRICKS

# 1    List with same items
list4 = [0] * 5
print(list4)

# 2   CONCATINATE TWO LIST
List3 = list1 + list2
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

# VI // IF WE COPY LIKE ABOVE CHANGES MADE TO ANY OF THE LIST WILL EFFECT BOTH EVEN AFTER ASSIGNMENT
# BECAUSE BOTH HAVE SAME MEMORY

# CORRECT WAY
list_copy = list_original.copy()
list_copy = list(list_original)
list_copy = list_original[:]

# 5. LIST COMPERHENSION
a = [1, 2, 3, 4, 5]
b = [i for i in a]  # = 1,2,3,4,5

list_name = [i ** 2 for i in a]  # a=list or any iterable

# 6.
print(list1.count(1))  # count no of times item repeated
#

#  7.
print(list1.index(2))  # gives position of item
