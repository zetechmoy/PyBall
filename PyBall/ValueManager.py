#-------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	04/10/2015
#-------------------------------------------------------------------------------
from abc import ABCMeta, abstractmethod

@abstractmethod
def save(key, value):

    with open("./data/config.balldat", "r") as f:
        lines = f.readlines()

    l = 0
    nbLine = len(lines)
    while l < nbLine:
        if(lines[l] == "\n"):
            lines.pop(l)
            nbLine -= 1
        l += 1

    l = 0
    nbLine = len(lines)
    while l < nbLine:
        if(lines[l].startswith(key)):
            lines.pop(l)
            nbLine -= 1
        l += 1

    lines.append("{} = {}".format(key, value))

    toWrite = ""
    for line in range(0, len(lines)):
        if (lines[line].endswith("\n")):
            lines[line] = lines[line][:-1]
        toWrite = toWrite + lines[line] + "\n"

    file = open("./data/config.balldat", "w")
    file.write(toWrite)
    file.close()

##    print ("toWrite :", toWrite)
##    print("lines (", len(lines),") :", lines)


@abstractmethod
def get(key, default):
    with open("./data/config.balldat", "r") as f:
        lines = f.readlines()
    for line in range(0,len(lines)):
        if lines[line].startswith(key):
            return lines[line].split("=")[1].strip()
    return default