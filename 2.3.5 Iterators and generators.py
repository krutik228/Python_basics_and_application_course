from math import factorial


def primes():
    p = 2
    while True:
        if ((factorial(p-1) + 1) % p) == 0:
            yield p
        p += 1


if __name__ == '__main__':
    y = primes()
    for i in range(31):
        print(next(y))
    # print(f(31))
