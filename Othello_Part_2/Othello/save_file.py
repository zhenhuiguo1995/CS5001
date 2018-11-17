import os
import sys


def save_file():
    file = open('scores.txt', 'w+')
    temp = []
    for line in file:
        print(line)
        #line = line.rstrip().split()
        #temp.append((line[0], line[1]))
    #temp.append((sys.argv[1], sys.argv[2]))
    #print(temp)
    #sorted(temp, key=lambda x: x[1], reverse=True)
    #for tuple in temp:
    #    file.write(tuple[0] + " " + tuple[1])


save_file()