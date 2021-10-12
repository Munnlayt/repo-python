def num_translate(en_word):
    en_word_book = {"one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять", "six": "шесть",
                    "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}
    if en_word.istitle():
        return en_word_book.get(en_word.lower()).title()
    return en_word_book.get(en_word)


print(num_translate(input('Введите число на английском с маленькой буквы \n')))