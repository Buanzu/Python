# Задание №1_____

class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def extractor(cls, date):
        day, month, year = map(int, date.split('-'))
        return day, month, year

    @staticmethod
    def valid(date_int):
        day, month, year = Date.extractor(date_int)
        if 2099 >= year <= 1900 or 12 > month < 1 or 1 > day > 31:
            return print('Не верная дата')
        elif month in (4, 6, 9, 11) and day > 30:
            return print('Не верная дата')
        elif (year % 400 != 0 and (year % 4 != 0 and year % 100 != 0)) and month == 2 and day > 28:
            return print('Не верная дата')
        else:
            return print('Верная дата')


print(Date.extractor('16-08-2022'))
Date.valid('31-05-1057')
Date.valid('31-04-3020')
Date.valid('32-11-2019')
Date.valid('28-02-2024')
Date.valid('29-02-2015')
Date.valid('20-02-2010')
Date.valid('31-01-2008')
Date.valid('15-07-2016')



# Задание №2_____

class Division_on_Null:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_on_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль невозможно")


div = Division_on_Null(10, 100)
print(Division_on_Null.divide_on_null(10, 0))
print(Division_on_Null.divide_on_null(10, 0.1))
print(div.divide_on_null(100, 0))

# Задание №3_____________

class IntException(Exception):
    def __init__(self):
        self.txt = 'Введено не число! '


res_list = []
while True:
    inp_user = input('Введите число или Enter для выхода ')
    if inp_user == '':
        break
    else:
        try:
            if inp_user.isdigit():
                res_list.append(int(inp_user))
            elif inp_user.count('.') > 1:
                raise IntException
            else:
                for sym in inp_user:
                    if not sym.isdigit() and sym != '.':
                        raise IntException
                res_list.append(float(inp_user))
        except IntException as err:
            print(err.txt)


# Задание № 4 - 6__________

from abc import ABC, abstractmethod


class Department(ABC):

    @abstractmethod
    def add(self, type_technic, data):
        pass


class MyTypeError(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class Storage:

    def __init__(self):
        self.__storage = {}

    @property
    def storage(self):
        return self.__storage

    def add_technic(self, technic, number):
        try:
            if not isinstance(number, int):
                raise MyTypeError('type of number must be int')
            technic.params['number'] = number
            if not self.__storage.get(technic.type_technic):
                self.__storage[technic.type_technic] = {technic.name: technic.params}
            else:
                self.__storage[technic.type_technic].setdefault(technic.name, technic.params)
        except MyTypeError as x:
            print(x)

    def transfer_to_department(self, technic, department):
        department.add(technic.type_technic, self.__storage.get(technic.type_technic))


class TransportDepartment(Department):

    def __init__(self):
        self.__storage = {}

    @property
    def storage(self):
        return self.__storage

    def add(self, type_technic, data):
        if not self.__storage.get(type_technic):
            self.__storage[type_technic] = data
        else:
            self.__storage[type_technic].setdefault(data)


class OfficeTechnics:

    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color


class Printer(OfficeTechnics):
    def __init__(self, name: str, color: str, speed: int):
        super().__init__(name, color)
        self.type_technic = self.__class__.__name__
        self.print_speed = speed
        self.params = {'name': self.name, 'color': self.color, 'print_speed': self.print_speed}


class Scanner(OfficeTechnics):
    def __init__(self, name: str, color: str, speed: int):
        super().__init__(name, color)
        self.type_technic = self.__class__.__name__
        self.scan_speed = speed
        self.params = {'name': self.name, 'color': self.color, 'scan_speed': self.scan_speed}


class Copier(OfficeTechnics):
    def __init__(self, name: str, color: str, speed: int):
        super().__init__(name, color)
        self.type_technic = self.__class__.__name__
        self.copy_speed = speed
        self.params = {'name': self.name, 'color': self.color, 'copy_speed': self.copy_speed}


if __name__ == '__main__':
    printer = Printer('HP', 'Black', 12)
    scaner = Scanner('Canon', 'White', 15)
    copier = Copier('Canon', 'Gray', 23)
    print(f'printer: {printer}')
    print(f'scaner: {scaner}')
    print(f'copier: {copier}')
    storage = Storage()
    storage.add_technic(printer, 20)
    storage.add_technic(scaner, 50)
    print(f'storage: {storage.storage}')
    transportDep = TransportDepartment()
    storage.transfer_to_department(scaner, transportDep)
    print(f'transportDep storage: {transportDep.storage}')

# Задание №7_______


