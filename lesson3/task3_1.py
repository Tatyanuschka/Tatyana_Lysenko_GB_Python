def num_translate(n):
    """translate numbers from English to Russian
    :type my_dict: object
    """
    my_dict = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    return my_dict.get(n) if n.islower() else my_dict.get(n.lower()).capitalize()


print(num_translate(input('Введите число на английском: ')))
