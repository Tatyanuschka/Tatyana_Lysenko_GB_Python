def thesaurus(*args):
    name_dict = {}
    for arg in args:
        if arg[0] not in name_dict:
            name_dict[arg[0]] = []
        name_dict[arg[0]].append(arg)
    return name_dict


print(thesaurus('Иван', 'Мария', 'Илья', 'Макс', 'Олег', 'София', 'Ольга', 'Олеся', 'Михаил', 'Сергей', 'Саша', 'Соня'))
