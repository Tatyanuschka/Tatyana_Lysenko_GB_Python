import pickle
import sys

with open('users.csv', 'r', encoding='utf-8') as f1:
    with open('hobby.csv', 'r', encoding='utf-8') as f2:
        fio_lst = [line for line in f1]
        # print(fio_lst)
        hobby_lst = [line for line in f2]
        # print(hobby_lst)
        k = len(fio_lst) - len(hobby_lst)
        # print(k)
        users_hobby = {}
        for i in range(len(fio_lst)):
            if k > 0 and i >= len(hobby_lst):
                users_hobby[fio_lst[i]] = None
            elif k < 0 or i < len(hobby_lst):
                users_hobby[fio_lst[i]] = hobby_lst[i]
        print(users_hobby)

with open('user_hobby.pickle', 'wb') as f:
    pickle.dump(users_hobby, f)
    if k < 0:
        sys.exit(1)

with open('user_hobby.pickle', 'rb') as f:
    result = pickle.load(f)
    print(result)


