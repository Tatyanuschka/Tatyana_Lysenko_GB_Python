amount = int(input('Введите количество промежутков времени: '))
for i in range (amount):
    s = int(input(f'Введите промежуток времени №{i + 1} в сек: '))
    while s < 0:
        s = int(input('Вы ввели отрицательное число, попробуйте еще раз: '))
    print(f'duration no.{i+1} = {s}')
    m = s // 60
    h = m // 60
    d = h // 24
    if s < 60:
        print(f'{s} сек')
    elif s < 3600:
        print(f'{m} мин {s % 60} сек')
    elif s < 86400:
        print(f'{h} час {m % 60} мин {s % 60} сек')
    elif s >= 86400:
        print(f'{d} дн {h % 24} час {m % 60} мин {s % 60} сек')
