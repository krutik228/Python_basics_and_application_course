import os.path


def main2():
    os.chdir(r'C:\Users\nikkr\Downloads\main')
    result = [cur_dir for cur_dir, _, files in os.walk('.') if any(file.endswith('.py') for file in files)]

    with open('result2.txt', 'w') as new_file:
        new_file.write('\n'.join(sorted(result)).replace('.\\', ''))


def main():
    new_file = open(r'.\result.txt', 'a')
    result = []
    os.chdir(r'C:\Users\nikkr\Downloads\main')
    for cur_dir, dirs, files in os.walk('.'):
        for file in files:
            if file[-3:] == '.py':
                result.append(cur_dir.replace('.\\', ''))
                break
    result = list(set(result))
    result.sort()
    for line in result:
        new_file.write(line + '\n')
    new_file.close()

if __name__ == '__main__':
    # main()
    main2()
