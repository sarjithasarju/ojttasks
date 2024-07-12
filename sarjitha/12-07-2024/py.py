import itertools

def combination(n):
    if n == 0:
        return
    else:
        digits = range(1, 10)
        for combo in itertools.combinations(digits, 3):
            print(combo)

combination(3)
