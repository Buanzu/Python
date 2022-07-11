_____________________________________________1_____________________________-__

my_list = [1.2, True, 10500, 'False', 33.33]


def my_type(element):
    for element in range(len(my_list)):
        print(type(my_list[element]))
    return


my_type(my_list)

______________________________________________2______________________________


element_count = int(input("Вводим количество элементов списка"))
my_list = []
a = 0
element = 0
while a < element_count:
    my_list.append(input("Вводим значение списка"))
    a += 1

for element in range(int(len(my_list)/2)):
    my_list[element], my_list[element + 1] = my_list[element+ 1], my_list[element]
    element +=2

    print(my_list)

______________________________________________3_______________________________

seazon_list = ["Зима", "Весна", "Лето", "Осень"]
seazon_dict = {1 : "Зима", 2 : "Весна", 3 : "Лето", 4 : "Осень"}
month = int(input("Вводим месяц с учетом номера "))
if month == 12 or month == 1 or month == 2:
    print(seazon_list[0])
    print(seazon_dict.get(1))

elif month == 3 or month == 4 or month == 5:
    print(seazon_list[1])
    print(seazon_dict.get(2))

elif month == 6 or month == 7 or month == 5:
    print(seazon_list[2])
    print(seazon_dict.get(3))

elif month == 9 or month == 10 or month == 11:
    print(seazon_list[3])
    print(seazon_dict.get(4))

else:
    print( "Вы ошиблись такого месяца нет")

_____________________________________________4_________________________________

my_string = input("Вводим предложение")
my_word = []
number = 1
for element in range(my_string.count(" ")+1):
    my_word = my_string.split()
    if len(str(my_word)) <= 10:
        print (f" {number} {my_word [element]}")
        number += 1

    else:
        print(f" {number} {my_word [element] [0 : 10]}")
        number += 1

____________________________________________5__________________________________

my_list = [7, 5, 4, 3, 1]
print(f"Рейтинг - {my_list}")
digit = int(input("Введите число (00 - выход) "))
while digit != 00:
    for element in range(len(my_list)):
        if my_list[element] == digit:
            my_list.insert(element + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[element] > digit and my_list[element + 1] < digit:
            my_list.insert(element + 1, digit)
    print(f"Текущий список - {my_list}")
    digit = int(input("Введите число (00 - выход) "))