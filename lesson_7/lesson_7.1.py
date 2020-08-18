# Урок 7 Задание 1

class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2


    def __add__(self):
        matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matr[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))


    def __str__(self,matr):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))


matrix_1 = Matrix([[2, 5, 7],
                    [12, 37, 25],
                    [1, 0, 3]],
                   [[5, 41, 33],
                    [67, 75, 3],
                    [2, 5, 9]])
print(matrix_1.__add__())