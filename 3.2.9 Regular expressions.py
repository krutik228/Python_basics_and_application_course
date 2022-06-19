def main():
    import sys
    import re

    pattern = r"z.{3}z"

    for line in sys.stdin:
        if re.search(pattern, line):
            print(line.rstrip())

def main2():
    import re
    import sys

    for line in sys.stdin:
        line = line.strip()
        if re.search(r"z...z", line):
            print(line)

if __name__ == '__main__':
    main()

