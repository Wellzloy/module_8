def add_everything_up(a, b):
    try:
        z = round((a + b), 3)
        return z
    except TypeError:
        return f'{a}{b}'


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))