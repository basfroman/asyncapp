def some_func(a, *, b):
    some_func.a = a
    return some_func


print(some_func(1, b=3).a)
