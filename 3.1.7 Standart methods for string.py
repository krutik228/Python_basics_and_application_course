
def main3():
    s, t = input(), input()
    return sum(s.startswith(t, i) for i in range(len(s)))


def main2():
    s, t = input(), input()
    return sum([s[i:i+len(t)] == t for i in range(len(s))])


def main():
    s, t = input(), input()
    l_t, l_s = len(t), len(s)
    i = 0
    count = 0
    while i < l_s:
        if s[i:i+l_t] == t:
            count += 1
        i += 1
    return count

if __name__ == '__main__':
    # print(main())
    print(main2())