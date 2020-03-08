#!/usr/bin/env python3

BABY_NAME_FILE = "babyname.txt"


import mmap
import sys
import json
from datetime import datetime

MONTHS = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

def getlastlines(fname, num_lines = 1):
    with open(fname) as source:
        mapping = mmap.mmap(source.fileno(), 0, prot=mmap.PROT_READ)
    prev_newline = mapping.rfind(b'\n', 0);
    for i in range(num_lines):
        prev_newline = mapping.rfind(b'\n', 0, prev_newline)
        if prev_newline == -1:
            break
    lines = mapping[prev_newline + 1:].decode('utf-8').split('\n')[:-1]
    return lines 

def main():
    try:
        if sys.argv[1] == "-p" or sys.argv[1] == "--partial":
            partial = True
        else:
            partial = False
    except IndexError:
        partial = False

    with open(BABY_NAME_FILE) as f:
        BABY_NAME = f.readline()[:-1]

    DATABASE = BABY_NAME.lower() + "-feedings.txt"
    now = datetime.now()

    last_ten_feedings = getlastlines(DATABASE, 10)
   
    all_feedings = []
    for feeding in last_ten_feedings:
        sentence = ""
        last_feeding = [int(x) for x in feeding.split(',')]

        if last_feeding[3] < 12:
            am = True
            if last_feeding[3] == 0:
                last_feeding[3] = 12
        else:
            am = False
            if last_feeding[3] > 12:
                last_feeding[3] -= 12

       
        if not partial:
            # sentence += BABY_NAME + " was last fed "
            if [now.month, now.day] == last_feeding[:2]:
                sentence += "today"
            elif now.day == last_feeding[1] + 1:
                sentence += "yesterday"
            else:
                sentence += "on " + MONTHS[last_feeding[0] - 1] + " " + str(last_feeding[1])
            sentence += " at "

        sentence += str(last_feeding[3]) + ":"
        sentence += str(last_feeding[4]).zfill(2)

        if am:
            sentence += " AM."
        else:
            sentence += " PM."

        all_feedings.append(sentence)

    print("Content-Type: application/json\n")
    print(json.dumps(all_feedings))

if __name__ == "__main__":
    main()
