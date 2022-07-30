import random

def get_random(input_list):
    if input_list:
        result = random.choice(input_list)
        return result

# для того чтобы при переносе в модуль main не выполнялся код нужно внести изменения
if __name__== '__main__':
    print(get_random([1, 2, 3, 4]))

# если список у нас пустой то мы должны
# вернуть None через else - return None
# однако в питоне если мы ничего не возвращаем то
# будет возвращаться NONE