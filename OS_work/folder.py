import os

# создаем папки
def create_folders():
    for i in range(1, 10):
        folder_name = f'dir_{i}'
        os.mkdir(folder_name)

# удаляем папки
def delete_folders():
    for i in range(1, 10):
        folder_name = f'dir_{i}'
        os.rmdir(folder_name)

# для того чтобы при переносе в модуль main не выполнялся код нужно внести изменения
if __name__== '__main__':
    create_folders()
    delete_folders()
