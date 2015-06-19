__author__ = 'alex'

f = file("curses.txt","r")

g = f.readlines()

h = []

for i in g[1:]:
    if len(i) > 10:
        line = i.split("\t")
        # print line
        h.append([line[0], line[1],line[2]])

print h
