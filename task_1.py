# ✔Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.
import os

def find_abspath(name: str):
    *path_name, extension = name.split('.')
    print(*path_name,'\n', extension)
    *path, name = ''.join(path_name).split("\\")
    return ('\\'.join(path), name, extension)

myfile = open(input('введите имя файла: '), 'w')
myfile.close()

print(find_abspath(os.path.abspath(myfile.name)))


# if os.path.exists('myfile.txt'):
#     print("Указанный файл существует")
# else:
#     print("Файл не существует")


# ___________ВЫВОД____________________
# введите имя файла: my.txt
# C:\Users\Home-PC\Лекции, семинары\13 Python series\hw_5\my
#  txt
# ('C:\\Users\\Home-PC\\Лекции, семинары\\13 Python series\\hw_5', 'my', 'txt')

