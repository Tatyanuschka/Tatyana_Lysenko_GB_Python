# функция создания списка сумм цифр каждого числа (элемента) из другого списка
def digit_sum(any_list):
    lst_sum = []
    for number in any_list:
        sum = 0
        while number > 0:
            d = number % 10
            number = number // 10
            sum += d
        lst_sum.append(sum)
    return lst_sum


cube_lst = []
for i in range(1, 1001, 2):
    cube_lst.append(i ** 3)
print(f'Список из кубов нечетн.чисел от 1 до 1000: {cube_lst}')

cube_lst_sum = digit_sum(cube_lst)
print(f'список чисел, сумма цифр к-ых делится на 7 без остатка: {cube_lst_sum}')

result_sum = 0
for i in range(len(cube_lst)):
    if cube_lst_sum[i] % 7 == 0:
        result_sum += cube_lst[i]
print(f'Сумма тех чисел, сумма цифр к-ых делится нацело на 7: {result_sum}')

result_sum = 0
cube_lst = [number + 17 for number in cube_lst]
cube_lst_sum = digit_sum(cube_lst)

for i in range(len(cube_lst_sum)):
    if cube_lst_sum[i] % 7 == 0:
        result_sum += cube_lst[i]
print(f'Сумма чисел (+17), сумма цифр к-ых делится нацело на 7: {result_sum}')
