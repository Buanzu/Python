while True:
    a = float(input("Введите a = стартовый результат: "))
    b = float(input("Введите b = финальный результат: "))
    result = 1
    if a <= 0 or b < 0:
        print("Результат должен быть больше нуля")
    else:
        while a < b:
            a += a * 0.1
            result += 1
        print (f'на {result} день атлет достиг результат')
        break