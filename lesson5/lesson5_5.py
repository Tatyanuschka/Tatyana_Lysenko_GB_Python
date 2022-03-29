from random import randint
from collections import Counter

src = [randint(1, 20) for i in range(40)]
print(src)
counter = Counter(src)
result = [key for key, val in counter.items() if val == 1]
print(result)
print(len(result))
