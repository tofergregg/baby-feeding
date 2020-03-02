#!/usr/bin/env python3

BABY_NAME_FILE = "babyname.txt"


import mmap
import sys
from datetime import datetime

MONTHS = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

def getlastline(fname):
    with open(fname) as source:
        mapping = mmap.mmap(source.fileno(), 0, prot=mmap.PROT_READ)
    return mapping[mapping.rfind(b'\n', 0, -1)+1:].decode('utf-8')

def main():
    try:
        if sys.argv[1] == "-p" or sys.argv[1] == "--partial":
            partial = True
        else:
            partial = False
    except IndexError:
        partial = False

    sentence = ""
    with open(BABY_NAME_FILE) as f:
        BABY_NAME = f.readline()[:-1]

    DATABASE = BABY_NAME.lower() + "-feedings.txt"
    now = datetime.now()

    last_feeding = [int(x) for x in getlastline(DATABASE)[:-1].split(',')]

    if last_feeding[3] < 12:
        am = True
        if last_feeding[3] == 0:
            last_feeding[3] = 12
    else:
        am = False
        if last_feeding[3] > 12:
            last_feeding[3] -= 12

   
    if not partial:
        sentence += BABY_NAME + " was last fed "
        if [now.month, now.day] == last_feeding[:2]:
            sentence += "today"
        elif now.day == last_feeding[1] + 1:
            sentence += "yesterday"
        else:
            sentence += "on " + MONTHS[now.month - 1] + " " + str(now.day)
        sentence += " at "

    sentence += str(last_feeding[3]) + ":"
    sentence += str(last_feeding[4]).zfill(2)
    if am:
        sentence += " AM."
    else:
        sentence += " PM."

    print(sentence)


if __name__ == "__main__":
    main()
