def  thesaurus(*args):
    a = {}
    for i in args:
        a.setdefault(i[0],[])
        a[i[0]].append(i)
    return a

print(thesaurus("Иван", "Мария", "Петр", "Илья", 'Артур', 'Петя', 'Маша', "Вася", "Алена", "Виктор", "Денис", "Влад"))

