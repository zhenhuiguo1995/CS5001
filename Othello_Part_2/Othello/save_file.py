import os
import sys


def save_file():
    if 'scores.txt' not in os.listdir():
        file = open('scores.txt', 'w+')
        temp = sys.argv[1] + sys.argv[2] + '\n'
        file.write(temp)
        file.close()
    else:
        file = open('scores.txt')
        temp = []
        for line in file:
            line = line.split()
            temp.append((line[0], int(line[1])))
        temp.append((sys.argv[1], int(sys.argv[2])))
        file.close()
        temp = sorted(temp, key=lambda x: x[1], reverse=True)
        file = open('scores.txt', 'w+')
        for pair in temp:
            line = pair[0] + ' ' + str(pair[1]) + '\n'
            file.write(line)
        file.close()

save_file()
