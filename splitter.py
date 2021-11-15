import os

global cwd
cwd = os.getcwd()

counter =1

lines_per_file = 5000
smallfile = None
with open(cwd + '\\sitandgos.txt') as bigfile:
    for lineno, line in enumerate(bigfile):
        if lineno % lines_per_file == 0:
            if smallfile:
                smallfile.close()
            small_filename = 'chapter{}.txt'.format(lineno)
            smallfile = open(small_filename, "w")
        smallfile.write(line)
    if smallfile:
        smallfile.close()