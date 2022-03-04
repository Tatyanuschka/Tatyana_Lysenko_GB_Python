def thesaurus_adv(*args):
    name_dict = {}
    for arg in args:
        name_fl, surname_fl = arg.split()[0][0], arg.split()[1][0]

        if surname_fl not in name_dict:
            name_dict[surname_fl] = {name_fl: [arg]}
        elif name_fl in name_dict[surname_fl]:
            name_dict[surname_fl][name_fl].append(arg)
        else:
            name_dict[surname_fl][name_fl] = [arg]
    return name_dict


print(
    thesaurus_adv('Иван Петров', 'Мария Куликова', 'Илья Лысенко', 'Макс Павлов', 'Олег Лучезарный', 'София Агафонова',
                  'Ольга Мишукова', 'Олеся Терехова', 'Михаил Алиев', 'Сергей Меличков', 'Саша Иванов',
                  'Марина Краснова', 'Таня Игнатова'))
