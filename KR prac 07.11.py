print("Задача №1: Написать декоратор, который посчитает количество вызовов функции. Декоратор должен применяться к нескольким функциям.")

def count_calls(func):
    calls = {}

    def wrapper(*args, **kwargs):
        name = func.__name__
        calls[name] = calls.get(name, 0) + 1
        return func(*args, **kwargs)

    wrapper.calls = calls
    return wrapper


@count_calls
def just_func(x):
    pass


@count_calls
def just_func2(y):
    pass


for i in range(3):
    just_func(2)
    just_func2(2)


print(f"Эта функция была вызвана {just_func.calls['just_func']} раз")
print(f"Эта функция была вызвана {just_func2.calls['just_func2']} раз")

print("Задание №2: Написать генератор бесконечной последовательности Фибоначи (сумма двух предыдущих)")

def fibonachi():
    a = 0
    b = 1

    while True:
        yield a
        a, b = b, a + b

fib = fibonachi()

for i in range(10):
    print(next(fib))


print("Задание №3: Написать quick sort")

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]

    left = []
    right = []
    middle = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            middle.append(x)

    return quick_sort(left) + middle + quick_sort(right)

numb = [4, 5, 3, 6, 7, 1, 10, 9, 8, 2]

print(quick_sort(numb))