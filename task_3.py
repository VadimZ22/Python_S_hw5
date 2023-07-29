# Создайте функцию генератор чисел Фибоначчи

def fibo_func(n):
    previos_num = 0
    current_num = 1
    next_num = None


    for i in range(n+1):
        yield previos_num
        next_num = previos_num + current_num
        previos_num = current_num
        current_num = next_num


for item in fibo_func(10):
    print(item)

# print(list(fibo_func(10)))