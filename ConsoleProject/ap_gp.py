# PROGRAM TO FIND AP, GP, SUM OF AP & GP


def ap():
    print("ARITHMETIC PROGRESSION")
    a = float(input("Enter the first number: "))
    d = float(input("Enter the common difference : "))
    n = int(input("Enter the number of terms: "))
    for i in range(n):
        term = a + i * d
        print(term, end=' ')


def gp():
    print("GEOMETRIC PROGRESSION")
    a = float(input("Enter the first number: "))
    d = float(input("Enter the common ratio : "))
    n = int(input("Enter the number of terms: "))
    for i in range(n):
        term = a * (d ** (i))
        print(term, end=' ')


def sum_ap():
    print("SUM OF ARITHMETIC PROGRESSION")
    a = float(input("Enter the first number: "))
    r = float(input("Enter the common difference : "))
    n = int(input("Enter the number of terms: "))
    sum_ap = 0

    for i in range(n):
        sum_ap = sum_ap + a + i * r

    print(sum_ap, end=' ')


def sum_of_gp():
    print("SUM OF GEOMETRIC PROGRESSION")
    a = float(input("Enter the first number: "))
    r = float(input("Enter the common ratio : "))
    n = int(input("Enter the number of terms: "))
    sum_gp = 0
    for i in range(n):
        sum_gp = sum_gp + (a * (r ** i))
    print(sum_gp)


def product_of_gp():
    print("PRODUCT OF GEOMETRIC PROGRESSION")
    a = float(input("Enter the first number: "))
    r = float(input("Enter the common ratio : "))
    n = int(input("Enter the number of terms: "))
    product_gp = 1
    for i in range(n):
        product_gp = product_gp * (a * (r ** i))
    print(product_gp)


if __name__ == "__main__":
    product_of_gp()
