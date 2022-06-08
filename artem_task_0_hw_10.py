def foo_1(a: int):
    x: int = a ** 2

    def foo_2():
        nonlocal x
        if x %2 == 0:
            b:str = f"квадрат числа {a} четное число "
        else:
            b:str = f"квадрат числа {a} не четное число"
        return b

    return foo_2()

o = foo_1(9)

print(o)