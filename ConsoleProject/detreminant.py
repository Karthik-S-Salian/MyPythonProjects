

a=[[1,2,3],
   [4,5,6],
   [7,8,9]]
b=[[1,2]]


def det(matrix):
    def error_check(matix):
        i = len(matix)

        for row in matix:
            if not len(row) == i:
                print('ENTERED MATRIX IS NOT SQUARE')
                quit(1)

    def divide(matrix, pos):
        matrix = matrix.copy()
        del matrix[0]
        if len(matrix) == 1:
            if pos == 1:
                return [matrix[0][0]]
            if pos == 0:
                return [matrix[0][1]]
        for row in matrix:
            del row[pos]
        return matrix


    def order(matrix):
        return len(matrix)


    def _det(matrix):
        i = 0
        if order(matrix) == 1:
            return matrix[0]
        s = 0
        for ele in matrix[0]:
            ele *= (-1) ** i
            s = s + ele * det(divide(matrix, i))
            i = i + 1
        return s
    error_check(matrix)
    _det(matrix)


if __name__=="__main__":
    det(a)