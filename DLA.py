import random

class CellAuto:
    def __init__(self, X, Y, procent):
        self.__X = X
        self.__Y = Y
        self.__procent = procent
        field = [[0] * X for i in range(Y)]
        self.__field = field
    """
    блок с инкапсуляцией и заданием значений
    """

    @property
    def field(self):
        return self.__field

    @property
    def X(self):
        return self.__X

    @X.setter
    def X(self, value):
        if value < 0:
            print('Значение не может быть меньше нуля')
        else:
            self.__X = value

    @property
    def Y(self):
        return self.__Y

    @Y.setter
    def Y(self, value):
        if value < 0:
            print('Значение не может быть меньше нуля')
        else:
            self.__Y = value

    @property
    def procent(self):
        return self.__procent

    @procent.setter
    def procent(self, value):
        if value < 0 or value > 100:
            print('Значение должно быть в диапазоне от 0 до 100')
        else:
            self.__procent = value

    def neighbours(self):
        for i in range(0, self.__X):
            for j in range(0, self.__Y):
                s=0
                for n in range(i-1,i+2):
                    for m in range(j-1,j+2):
                        if (n==i and m==j) or n==-1 or m==-1 or n==self.__X or m==self.__Y:
                            continue
                        elif self.__field[m][n] == 1:
                            s+=1

                if self.__field[j][i] == 1:
                    if s == 2 or s == 3:
                        self.__buffer[j][i] = 1
                    else:
                        self.__buffer[j][i] = 0
                elif self.__field[j][i] == 0:
                    if s == 3:
                        self.__buffer[j][i] = 1
                    else:
                        self.__buffer[j][i] = 0

    def update(self, cell_auto):
        for i in range(0, self.__X):
            for j in range(0, self.__Y):
                if random.randint(1,100) <= self.__procent:
                    self.__field[j][i] = 1
        display(self.__field)


class DLA(CellAuto):
    def __init__(self, X, Y, procent):
        super().__init__(X, Y, procent)

    def update(self, cell_auto):
        self.__field = self.field
        self.__X = self.X
        self.__Y = self.Y
        self.__procent = self.procent
        self.__field[(self.__Y//2)][self.__X//2] = 1
        display(self.__field)
        number_cells = 1

        while number_cells / (self.__X * self.__Y) * 100 < self.__procent:
            number_cells = 0
            for i in range(0, self.__X):
                for j in range(0, self.__Y):
                    if self.__field[j][i] == 1:
                        number_cells += 1

            while True:
                X1 = random.randint(0, self.__X - 1)
                Y1 = random.randint(0, self.__Y - 1)
                if self.__field[Y1][X1] == 0:
                    self.__field[Y1][X1] = '*'
                    display(self.__field)
                    break

            while self.__field[Y1][X1] != 1:
                self.__field[Y1][X1] = 0
                cell_auto.neighbours(Y1, X1)

                if self.__field[Y1][X1] != 1:
                    k = random.randint(0, 3)
                    if k == 0:
                        Y1 -= 1
                    elif k == 1:
                        X1 -= 1
                    elif k == 2:
                        Y1 += 1
                    elif k == 3:
                        X1 += 1
                    if X1 == -1 or Y1 == -1 or X1 == self.__X or Y1 == self.__Y:
                        display(self.__field)
                        break
                    else:
                        self.__field[Y1][X1] = '*'
                display(self.__field)


    def neighbours(self,Y1,X1):
        for n in range(X1 - 1,X1 + 2):
            for m in range(Y1 - 1, Y1 + 2):
                if n == -1 or m == -1 or n == self.__X or m == self.__Y or (n!= X1 and m != Y1):
                    continue
                elif self.__field[m][n] == 1:
                    self.__field[Y1][X1] = 1
                    break

def display(field):
        for i in range(0, len(field)):
            for j in range(0, len(field[i])):
                print(field[i][j], end=' ')
            print()
        print()

def get_params():
    width = (input('Введите ширину матрицы: '))
    while width.isnumeric() == 0:
        print('Введите корректное значение, типа int')
        width = input('Введите ширину матрицы: ')
    width = int(width)

    height = (input('Введите высоту матрицы: '))
    while height.isnumeric() == 0:
        print('Введите корректное значение, типа int')
        height = input('Введите высоту матрицы: ')
    height = int(height)

    procent = (input('Введите процентное содержание частиц: '))
    while procent.isnumeric() == 0:
        print('Введите корректное значение, типа int')
        procent = input('Введите процентное содержание частиц: ')
    procent = int(procent)
    return width,height,procent

def main():
    width, height, procent = get_params()
    dla1 = DLA(width, height, procent)
    dla1.update(dla1)

main()