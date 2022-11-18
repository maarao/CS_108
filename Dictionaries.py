d = {}
d[3] = 7
d['cat'] = 8
d[5] = 9
d[500] = 'spam'
d[17] = 6

print(d)

from bakery import assert_equal

def reduced_to_one(char, text):
    count = 0
    removed = ''
    for t in text:
        if char == t:
            count += 1
            if count <= 1:
                removed += t
        else:
            count = 0
            removed += t
    return removed

assert_equal(reduced_to_one('a', 'aaababa'), 'ababa')