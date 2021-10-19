src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


temp = set()
unique_src = set()

for i in src:
    if i not in temp:
        unique_src.add(i)
    else:
        unique_src.discard(i)
    temp.add(i)
print(unique_src)
