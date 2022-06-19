import re


def main():
    import sys
    import re

    pattern = r".*\bcat\b"

    for line in sys.stdin:
        if re.match(pattern, line):
            print(line.rstrip())

def main2():
    import re
    import sys

    for line in sys.stdin:
        line = line.rstrip()
        if re.search(r"\bcat\b", line):
            print(line)

if __name__ == '__main__':
    main()