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







