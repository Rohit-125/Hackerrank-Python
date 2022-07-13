def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

import re

from functools import reduce
def score_words(words):
   return reduce(lambda x, y: x + y, [2 if (len(re.findall('[aeiouy]', a))%2 == 0) else 1 for a in words], 0)


n = int(input())
words = input().split()
print(score_words(words))
