with open('users.csv', 'r', encoding='utf-8') as f1:
    with open('hobby.csv', 'r', encoding='utf-8') as f2:
        with open('users_hobby.txt', 'a', encoding='utf-8') as f3:
            for line in zip(f1, f2):
                new_line = line[0][:-1] + ': ' + line[1]
                f3.write(new_line)