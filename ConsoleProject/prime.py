print("PROGRAM TO CHECK WEATHER A NUMBER IS PRIME OR NOT\n")
num = float(input("Enter a number: "))

# main loop
i = 2
while i <= num / 2:
    i = i + 1
    if num % i == 0:
        print("It is  not a prime number")
        exit()
print("It is  a prime number")
