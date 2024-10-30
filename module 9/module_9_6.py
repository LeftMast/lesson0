from itertools import combinations


def all_variants(text):
    for r in range(1, len(text) + 1):
        for lst in combinations(text, r):
            yield ''.join(lst)


a = all_variants("abc")
for i in a:
    print(i)