employers = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
             'директор аэлита']
print(employers)
for member in employers:
    position = member.split(' ')
    name = position[-1].capitalize()
    print(f'Привет. {name}!')
