

def main():
    def is_parent(parent, child, tree):
        if (parent == child) or (parent in tree[child]):
            return 'Yes'
        if tree[child]:
            for p in tree[child]:
                if is_parent(parent, p, tree) == 'Yes':
                    return 'Yes'
        return 'No'

    d = {}

    n = int(input())
    for _ in range(n):
        a = input().split()
        d[a[0]] = [] if len(a) == 1 else a[2:]

    m = int(input())
    for _ in range(m):
        a, b = input().split()
        print(is_parent(a, b, d))


def main2():
    n = int(input())
    parents = {}
    for _ in range(n):
        a = input().split()
        parents[a[0]] = [] if len(a) == 1 else a[2:]

    def is_parent(parent, child):
        return child == parent or any(map(lambda p: is_parent(parent, p), parents[child]))

    q = int(input())
    for _ in range(q):
        a, b = input().split()
        print("Yes" if is_parent(a, b) else "No")


def main3():
    n = int(input())
    parents = {}
    for _ in range(n):
        a = input().split()
        parents[a[0]] = [] if len(a) == 1 else a[2:]

    def is_parent(parent, child):
        return child == parent or any([is_parent(parent, p) for p in parents[child]])

    q = int(input())
    for _ in range(q):
        a, b = input().split()
        print("Yes" if is_parent(a, b) else "No")



if __name__ == '__main__':
    main()
    # main2()
    # main3()
