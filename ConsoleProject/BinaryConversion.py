print("CONVERSION OF DECIMAL NUMBER TO BINARY NUMBER")


def int_convert(value):
    remainder_list = list()
    while value>0:
        remainder_list.append(value % 2)
        value = int(value / 2)
    remainder_list.reverse()
    print(remainder_list)


def decimal_convert(value, l):
    int_list=list()
    value = value / (10 ** l)
    for i in range(6):
        value*=2
        x= int(value)
        int_list.append(x)
        print(value)
        value=value-x
    print(int_list)



def string_to_int(value):
    snum_list = value.split(".")
    snum_list.append(0)

    if len(snum_list) > 3:
        print("NUMBER_ERROR")
        quit(1)

    try:
        int_convert(0 + int(snum_list[0]))
        decimal_convert(0 + int(snum_list[1]), len(snum_list[1]))
    except:
        print("ENTER_NUMBERS_ONLY")


if __name__ == "__main__":
    string_to_int(input("Enter the number to be converted: "))
