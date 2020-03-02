#!/usr/bin/env python3

from datetime import datetime, timedelta

BABY_NAME_FILE = "babyname.txt"

def main():
    with open(BABY_NAME_FILE) as f:
        BABY_NAME = f.readline()[:-1]
    DATABASE = BABY_NAME.lower() + "-feedings.txt"

    print("Content-Type: text/plain\n")

    # now = datetime.now() - timedelta(hours=1, minutes=0)
    now = datetime.now()
    date_time = now.strftime("%m,%d,%Y,%H,%M\n")

    with open(DATABASE, 'a') as f:
        f.write(date_time)

    print("Last feeding: " + date_time)

if __name__ == "__main__":
    main()

