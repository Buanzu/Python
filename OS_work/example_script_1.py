import sys, os


def ping():
    print('pong')


ping()

def hello(name):
    print('Hello', name)


hello('Leo')



def get_info():
    print(os.listdir())


get_info()

command = sys.argv[1]

if command == 'ping':
    ping()
elif command == 'list':
    get_info()
elif command == 'name':
   # вводим второй аргумент в скрипт "имя"
    name = sys.argv[2]
    hello(name)