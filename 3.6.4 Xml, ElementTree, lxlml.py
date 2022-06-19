from xml.etree import ElementTree


def main():
    colors = {'red': 0, 'green': 0, 'blue': 0}
    string = input()
    root_ = ElementTree.fromstring(string)

    def getChildren(root, level=1):
        colors[root.attrib['color']] += level
        for child in root:
            getChildren(child, level + 1)

    getChildren(root_)
    print(*colors.values())

if __name__ == '__main__':
    main()
