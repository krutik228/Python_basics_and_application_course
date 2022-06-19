import shutil
import os.path

'''Перенос всех .txt файлов из текущей директории в папку ./tests'''

for cur_dir, _, files in os.walk('.'):
    for file in files:
        if cur_dir == '.' and file.title()[-3] == 'txt':
            shutil.move(file, './tests')
