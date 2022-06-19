a = [int(item) for item in input("Enter the list item: ").split(',')]
b = []
n = len(a)
p = n - 1
large = 0
for i in range(n):

    c = []
    for l in range(n):
        c.append(a[l])
    for j in range(p):
        if c[j] > c[j + 1]:
            c[j + 1] = c[j]
        if j == (p - 1):
            if c[p] > c[p - 1]:
                large = c[p]
            else:
                large = c[p - 1]
            for k in range(n):
                if large == a[k]:
                    a[k]=0
    b.append(large)
print("SORTED ARRAY : ")
print(b)
