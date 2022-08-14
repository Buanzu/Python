# Задание_№1________

a = [[2, 3, 4, 8], [3, 1, 5, 7], [8, 5, 7, 4]]
b = [[3, 1, 3, 4], [5, 2, 4, 6], [7, 4, 5, 6]]


class Matrix:

    def __init__(self, lists):
        self.lists = lists

    def __add__(self, other):
        d = []
        for n in range(len(self.lists)):
            d.append([])
            for c in range(len(self.lists[0])):
                d[n].append(self.lists[n][c] + other.lists[n][c])
        return '\n'.join(map(str, d))


matrix_1 = Matrix(a)
matrix_2 = Matrix(b)
print(f'Matrix 1\n{matrix_1}\n{" " * 30}')
print(f'Matrix 2\n{matrix_2}\n{" " * 30}')
print(f'matrix 1 + matrix 2\n{matrix_1 + matrix_2}')


# Задание_№2____________

from abc import ABC, abstractmethod


class Clothes(ABC):
    calculation = 0

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def consumtion(self):
        pass

    def __add__(self, other):
        Clothes.calculation += self.consumtion + other.consumtion
        return Costume(0)

    def __str__(self):
        res = Clothes.calculation
        Clothes.calculation = 0
        return f"{res}"


class Coat(Clothes):
    @property
    def consumtion(self):
        return round(self.param / 6.5) + 0.5


class Costume(Clothes):
    @property
    def consumtion(self):
        return round((2 * self.param + 0.3) / 100)


coat = Coat(50)
costume = Costume(180)
print(coat + costume + coat)

# Задание №3___________


class Cell:
    def __init__(self, nums):
        self.nums = nums

    def order(self, rows):
        return '\n'.join(['**' * rows for _ in range(self.nums // rows)]) + '\n' + '$$' * (self.nums % rows)

    def __str__(self):
        return f"{self.nums}"

    def __add__(self, other):
        print("Sum of cell = ")
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print("Subtraction of cell = ")
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 \
            else "Ячеек в первой клетке меньше чем во второй, вычесть невозможно!"

    def __mul__(self, other):
        print("Multiply of cell is:")
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        print("Truediv of cell is:")
        return Cell(self.nums // other.nums)