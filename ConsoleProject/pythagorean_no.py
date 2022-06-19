from  math import sqrt

print("PYTHAGOREAN NUMBERS")

limit=int(input('Enter the number limit: '))

for i in range(1,limit):
    for j in range(i,limit):
        c_sqr=i**2 + j**2
        c=int(sqrt(c_sqr))
        if c**2==c_sqr:
            print(i,j,c)