def my_fun(num_1, num_2):
    try:
        return num_1/num_2
    except ZeroDivisionError:
        print(f'Делить на ноль нельзя!')


print(my_fun(int(input('Первое число: ')), int(input('Второе число: '))))



def div(v_1, v_2):
    try:
        v_1, v_2 = int(v_1), int(v_2)
        div_num = v_1 / v_2
    except ValueError:
        return "Ошибка значения!"
    except ZeroDivisionError:
        return "Деление на ноль запрещено!"
    return round(div_num, 4)


print(div(input("Введите первое число -"), input("Введите второе число - ")))


_____________________________________________2___________________________________________________

def personal_data(name, lastname, year_of_birth, city, email, phone, place_of_work):
    return f"Имя - {name} Фамилия - {lastname} Год рождения - {year_of_birth}'" \
           f"Город проживания - {city} Email - {email} Телефон - {phone}  Место работы - {place_of_work}"


print(personal_data(name="Max", lastname="Mitrofanov", year_of_birth="1985", city="Vladivoctok",
                    email="mitrofanovmv@yandex.ru",
                    phone="89146966630", place_of_work="PCOD"))



_____________________________________________3_____________________________________________________

def my_fun(nam_1, nam_2, nam_3):
    return sum(sorted([nam_1, nam_2, nam_3])[1:])

print(my_fun(4, 10, 98))


def my_func(num_1, num_2, num_3):
    print(f'Сумма двух наибольших аргументов равна: {num_1 + num_2 + num_3 - min([num_1, num_2, num_3])}')


my_func(int(input('Число 1:')), int(input('Число 2:')), int(input('Число 3:')))

______________________________________________4______________________________________________________


def my_pow_fun(a, b):
    try:
        res = a ** b
    except TypeError:
        return "Enter float number and negative power"
    return res

print(my_pow_fun(14, -4))

______________________________________________5_______________________________________________________

def sum_num():
    n = 0
    while True:
        err = False
        in_list = input("Введите число, введите 'w' для выхода: ").split()
        for num in in_list:
            if num.lower() == "w":
                return n
            else:
                try:
                    n += int(num)
                except ValueError:
                    err = True
        if err:
            print("Данные неверны!")
        print(f"Сумма чисел = {n}")


print(sum_num())

________________________________________________6________________________________________________________

def int_func():
    for word in input("Ведите слова разделенные пробелом(нижний латинский регистр):\n").split():
        chars = 0
        for char in word:
            if 97 <= ord(char) <= 122:
                chars += 1
        print(word.title() if chars == len(word) else f"{word} - только прописные латинские буквы!")

int_func()