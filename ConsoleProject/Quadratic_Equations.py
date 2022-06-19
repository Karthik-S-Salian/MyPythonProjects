from math import sqrt
def quadratic(a, b, c):
    discriminant=b * b - 4 * a * c
    if discriminant >= 0:
        root=sqrt(discriminant)
        return (-b + root) / (2 * a), (-b - root) / (2 * a)
    else:
        root = round(sqrt(-discriminant),4)
        return f"({-b} + {root}i)/{2*a} ,({-b} + {root}i)/{2*a}"

print(quadratic(4,6,4))
