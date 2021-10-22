from itertools import zip_longest

with open('hobby.csv', 'r', encoding='utf-8') as f:
    hobbys = (f.read().split('\n'))

with open('users.csv', 'r', encoding='utf-8') as n:
    users = (n.read().split('\n'))

with open('users_hobby.txt', 'w') as f:
    for user, hobby in zip_longest(users, hobbys):
        if user == None:
            f.write('1')
            break
        f.write(f'{user} : {hobby}\n')
        print(f)
