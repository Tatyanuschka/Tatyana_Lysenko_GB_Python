from random import choice, shuffle


def get_jokes(n, no_repeat=True):
    """
    function of jokes' creating consisting of 3 words
    :param n: amount of jokes
    :param no_repeat: without repeating words from joke to joke (default) and with repeating (False)
    :return: list of "n" jokes
    """
    nouns = ["сугроб", "кофе", "дом", "сарай", "ключ", "торшер", "унитаз", "мост", "лист", "баран"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "рано утром", "весной", "в следующем году",
               "однажды", "давичи"]
    adjectives = ["холодный", "волшебный", "зеленый", "воздушный", "отчаянный", "заметный", "тревожный", "лучший",
                  "хозяйственный", "скользкий"]
    jokes = []
    if no_repeat:  # jokes without repeating words in them
        shuffle(nouns)
        shuffle(adverbs)
        shuffle(adjectives)
        for i in range(n):
            joke = f'{nouns[i]} {adverbs[i]} {adjectives[i]}'
            jokes.append(joke)
    else:
        for i in range(n):  # jokes where words can be repeated
            noun, adverb, adjective = choice(nouns), choice(adverbs), choice(adjectives)
            joke = f'{noun} {adverb} {adjective}'
            jokes.append(joke)

    for el in jokes:
        print(el, '\n')

    return jokes


print(get_jokes(10))
