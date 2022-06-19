from math import pow

num2 = 0
num1 = float(input("Enter: "))

while True:
    ch = input()
    if ch == "+":
        num2 = float(input())
        num1 += num2
    elif ch == "-":
        num2 = float(input())
        num1 -= num2
    elif ch == "/":
        num2 = float(input())
        num1 /= num2
    elif ch == "*":
        num2 = float(input())
        num1 *= num2
    elif ch == "^":
        num2 = float(input())
        pow(num1, num2)
    elif ch == "=":
        print(num1)
        break
    else:
        print("INVALID_OPERATOR")
        break
