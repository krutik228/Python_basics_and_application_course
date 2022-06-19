

def main():
    s = input()
    a = input()
    b = input()
    count_ = 0
    while s.count(a) > 0:
        s = s.replace(a, b)
        count_ += 1
        if count_ > 1000:
            return 'Impossible'
    return count_


if __name__ == '__main__':
    print(main())