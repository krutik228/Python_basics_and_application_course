
def is_parent(parent, child, tree):
    if parent == child or parent in tree[child]:
        return True
    if tree[child]:
        for p in tree[child]:
            if is_parent(parent, p, tree):
                return True
    return False


def read_std(string: str):
    return string.replace(' : ', ' ').split()


def main():
    tree = {}
    n = int(input())
    for _ in range(n):
        lst = read_std(input())
        tree.update({lst[0]: lst[1::]})

    m = int(input())
    buffer = []
    for _ in range(m):
        error = input()
        if any(map(lambda p: is_parent(p, error, tree), buffer)):
            print(error)
        buffer.append(error)


if __name__ == '__main__':
    main()
