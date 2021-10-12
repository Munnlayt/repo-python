import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(n):
    jokes = []
    for i in range(n):
        jokes.append(random.choice(nouns) + ' ' + random.choice(adverbs) + ' ' + random.choice(adjectives))
    return jokes

print(get_jokes(4))

