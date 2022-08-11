# Задание № 1 ____________________________________________
with open('test_text.txt', 'w', encoding='utf-8') as my_f:
    while True:
        my_line = input('Введите новую стоку или пропустите строку для окончания ввода данных')
        if not my_line:
            break
            print(my_line, file=my_f)


# Задание № 2 _____________________________________________

with open('test_text_1.txt', 'r', encoding='utf-8') as my_f:
    correct = [f'{count}. {line.strip()} - {len(line.split())} слов' for count, line in enumerate(my_f, 1)]
    print(*correct, f'Итого строк - {len(correct)}.', sep="\n")


# Задание №3 ______________________________________________

with open('test_text_2.txt', 'r', encoding='utf-8') as my_f:
    slaves_dict = {line.split()[0]: float(line.split()[1]) for line in my_f}
    print(f'Средняя зарплата = {round(sum(slaves_dict.values()) / len(slaves_dict), 3)}\n'
          f'"Денег нет, но вы держитесь!", до 20к {[i[0] for i in slaves_dict.items() if i[1] < 20000]}')


# Задание № 4______________________________________________

my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре", "Five": "Пять"}

with open("test_text_4.txt", 'w', encoding='utf-8') as file_1:
    with open("test_text_4.txt", encoding='utf-8') as file_2:
        file_2.writelines([line.replace(line.split()[0], my_dict.get(line.split()[1])) for line in file_2])


# Задание № 5______________________________________________

from random import randint
with open("test_text_5.txt", 'w', encoding='utf-8') as new_file:
    list = [randint(1, 200) for _ in range(200)]
    new_file.write(" ".join(map(str, list)))

print(f"Сумма элементов - {sum(list)}")

# Задание № 6_______________________________________________

new_dict = {}
with open("test_text_6.txt", encoding="utf-8") as f_obj:
    for line in f_obj:
        name, stats = line.split(':')
        name_sum = sum(map(int, "".join([i for i in stats if i == ' ' or '9' >= i >= '0']).split()))
        new_dict[name] = name_sum
    print(f'{new_dict}')

# Задание № 7_______________________________________________

import json
with open("ex_7.json", 'w', encoding="utf-8") as write_f, open("test_text_7.txt", encoding="utf-8") as my_file:
    income = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in my_file}
    f_up = [n for n in income.values() if n > 0]
    result = [income, {"real_income": round(sum(f_up) / len(f_up))}]

    json.dump(result, write_f, ensure_ascii=False, indent=4)