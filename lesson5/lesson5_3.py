tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Катя'
]
classes = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '11Б'
]

result = ((tutors[i], None) if i >= len(classes) else (tutors[i], classes[i]) for i in range(len(tutors)))
# print(*result)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))


