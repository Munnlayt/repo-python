tu = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
kl = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def gen(a):
    for i in range(a):
        if len(kl) < i + 1:
            kl.append("None")
        yield tu[i] + kl[i]


a = gen(len(tu))
for i in a:
    print(i)
