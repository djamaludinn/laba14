from random import randint

try:
    import random

    a = int(input('строки -> '))
    b = int(input('столбцы -> '))
    c = int(input('начало диапазона целых чисел -> '))
    d = int(input('конец диапазона целых чисел -> '))
    lst = [[randint(c, d) for i in range(a)] for i in range(b)]
    for i in lst:
        print()
        for j in i:
            print(j, end=" ")
except ValueError:
    print("Ошибка, повторите снова!")
else:
    print("\nВыполняется, если не было ошибок!")
finally:
    print("Выполняется всегда!")