

# from abc import ABC, abstractmethod
#
#
# class Clothes(ABC):
#     calculation = 0
#
#     def __init__(self, param):
#         self.param = param
#
#     @property
#     @abstractmethod
#     def consumtion(self):
#         pass
#
#     def __add__(self, other):
#         Clothes.calculation += self.consumtion + other.consumtion
#         return Costume(0)
#
#     def __str__(self):
#         res = Clothes.calculation
#         Clothes.calculation = 0
#         return f"{res}"
#
#
# class Coat(Clothes):
#     @property
#     def consumtion(self):
#         return round(self.param / 6.5) + 0.5
#
#
# class Costume(Clothes):
#     @property
#     def consumtion(self):
#         return round((2 * self.param + 0.3) / 100)
#
#
# coat = Coat(50)
# costume = Costume(180)
# print(coat + costume + coat)

# class Cell:
#     def __init__(self, nums):
#         self.nums = nums
#
#     def order(self, rows):
#         return '\n'.join(['**' * rows for _ in range(self.nums // rows)]) + '\n' + '$$' * (self.nums % rows)
#
#     def __str__(self):
#         return f"{self.nums}"
#
#     def __add__(self, other):
#         print("Sum of cell = ")
#         return Cell(self.nums + other.nums)
#
#     def __sub__(self, other):
#         print("Subtraction of cell = ")
#         return  Cell(self.nums - other.nums) if self.nums - other.nums > 0 \
#             else "Ячеек в первой клетке меньше чем во второй, вычесть невозможно!"
#
#     def __mul__(self, other):
#         print("Multiply of cell is:")
#         return Cell(self.nums * other.nums)
#
#     def __floordiv__(self, other):
#         print("Truediv of cell is:")
#         return Cell(self.nums // other.nums)
#
#
# cell_1 = Cell(20)
# cell_2 = Cell(30)
# print(cell_1 + cell_2)
# print(cell_1 - cell_2)
# print(cell_1 * cell_2)
# print(cell_1 // cell_2)
# print(cell_2.order(7))
#
