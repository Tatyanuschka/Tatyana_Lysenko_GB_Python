import random

prices = [round(random.uniform(1, 2000), 2) for i in range(20)]
print(prices)
print(f'id первоначального списка: {id(prices)}')
prices.sort()
print(prices)
print(f'id отсротированного по возрастанию списка: {id(prices)}')
prices_new = sorted(prices, reverse=True)
print(prices_new)
for price in prices:
    price = str(price)
    price_part = price.split('.')
    print(f'{int(price_part[0]):02d} руб {int(price_part[1]):02d} коп', end=', ')
print()
print('5 самых дорогих товаров:')

prices_new = prices_new[:5]

prices_new.sort()
for price in prices_new:
    price = str(price)
    price_comp = price.split('.')
    print(f'{int(price_comp[0]):02d} руб {int(price_comp[1]):02d} коп', end=', ')
