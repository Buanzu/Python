revenue = float(input("Введите значение прибыли фирмы (рубли) - "))
costs = float(input("Введите значение издежек фирмы (рубли) -"))
result = revenue - costs
if result > 0:
    print(f"Bingo! Вы работаете с прибылью {result} рублей")
    print(f"Рентабильность составила {100 * (result / costs):.1f}")
    personal_num = int(input("Количество сотрудников в офисе компании "))
    print(f"Прибыль фирмы на каждого сотрудника {result / personal_num:.3f} рублей")
elif result < 0:
    print(f"Компания сработала с убытком {-result} рублей. Направьте сотрудников на обучение в GeekBrains")
else:
    print("Think different!")
