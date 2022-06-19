print("PROGRAM TO FIND WEATHER A NUMBER IS INTEGRAL POWER OF GIVEN NUMBER OR NOT")


def check(num, base):
    a = base
    while a < num:
        a = a * base
    if a == num:
        print("It is a integral power of ", base)
    else:
        print("It is not a integral power of ", base)


check(float(input("Enter number: ")), float(input("Enter base: ")))
