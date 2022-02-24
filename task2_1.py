exp_lst = {'15*3': 15 * 3, '15/3': 15 / 3, '15 // 2': 15 // 2, '15**2': 15 ** 2}
for key, val in exp_lst.items():
    print(f'тип результата выражения {key} - {type(val)}')
