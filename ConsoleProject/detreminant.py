

a=[[1,2,3],
   [4,5,6],
   [7,8,9]]
b=[[1,2]]
def error_check(matix):
    i=len(matix)

    for row in matix:
        if not len(row)==i:
            print('ENTERED MATRIX IS NOT SQUARE')
            quit(1)

error_check(b)



