import json


def main():
    json_ = json.loads(input())

    tree = {}

    [tree.update({_class['name']: _class['parents']}) for _class in json_]

    def is_parent(parent, child):
        return child == parent or any([is_parent(parent, parents_of_child) for parents_of_child in tree[child]])

    counter = {}

    for node_i in tree:
        count = 0
        for node_j in tree:
            if is_parent(node_i, node_j):
                count += 1
        counter.update({node_i: count})

    [print(f"{name} : {count}") for name, count in sorted(counter.items())]


if __name__ == '__main__':
    main()
