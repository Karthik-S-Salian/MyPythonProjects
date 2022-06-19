def recursive_factorial(n, __x=1):
    if n < 2:
        if n <= 0:
            return 1
        __x *= n
    return recursive_factorial(n - 1, __x)


def factorial(num):
    product = 1
    for i in range(1, num + 1):
        product *= i
    return product
