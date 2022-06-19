# sort list using for loop
a = list()
while True:
    try:
        a = [int(item) for item in input("Enter the number: ").split(',')]
        break
    except:
        print("Entered item is not a number")

print("list before sorting: ", a)
large = None
b = a.copy()
c = list()
for n in a:
    large = b[0]
    for num in b:
        if num >= large:
            large = num
    b.remove(large)
    c.append(large)

print("Sorted list : ", c.reverse())
