
def main():
    import re
    import sys


    pattern = r"(cat)"

    for line in sys.stdin:
        line = line.rstrip()
        if len(re.findall(pattern, line)) > 1:
            print(line)

def main2():
    import re
    import sys

    for line in sys.stdin:
        line = line.strip()
        if re.search(r"cat.*cat", line):
            print(line)

if __name__ == '__main__':
    main()