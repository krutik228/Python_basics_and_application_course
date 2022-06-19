"""Копирование содержимого файла в обратном порядке в другой файл"""

with open(r'C:\Users\nikkr\Downloads\dataset_24465_4 (2).txt') as f, open('copy.txt', 'w') as w:
    for line in f.readlines()[::-1]:
        w.write(line)
