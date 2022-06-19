
#   is
#   is is similar to == but more precise than ==
# 'is' is used only to compare None,True,False or other which has only one form


def is_and_equals():
    x = None
    if x is None:
        print("None")

    # (0 != 0.0 using is because int != float)
    if 1 == 1.0:
        print("True")

    veg = "tomato"

    if "a" in veg:
        print("True")

    # break -> terminates out of the loop         # works only in loop

    # continue -> skips current iteration to next     # works only in loop

    for x in range(10):

        if x == 5:
            print("continue")
            continue

        if x == 9:
            print("break")
            break

        print("pass")

def asterisk():

    ones=[1]*5  # create list with 5 elments of 1
    zeros=(0)*5   # create tuple with 5 elments of 0

    list1=[0,1]*10  # repeats elements contains double of 10

    word="AB"*10

    print(ones,zeros,list1,word,sep="\n")

if __name__=="__main__":
    asterisk()