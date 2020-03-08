#!/usr/bin/env python3

from datetime import datetime, timedelta
import sys
import json
import cgi
import cgitb
cgitb.enable()

BABY_NAME_FILE = "babyname.txt"

def main():
    try:
        if sys.argv[1] == '-g' or sys.argv[1] == '--google-voice':
            google_voice = True
        else:
            google_voice = False
    except IndexError:
        google_voice = False
    print("Content-Type: text/plain\n")
    # for FieldStorage() to work,
    # needed to change line 704 in /usr/lib/python3.7/cgi.py to:
    # self.file.write(data.encode('utf-8')
    try:
        form = json.loads(sys.stdin.read())
    except json.decoder.JSONDecodeError:
        form = {} 
    
    try:
        hour = form['hour']
        minute = form['minute']
        meridian = form['meridian']
    except KeyError:
        hour = "--" 
        minute = "--"
        meridian = "--"

    if hour != "--":
        hour = int(hour)
    if minute != "--":
        minute = int(minute)

    if meridian.lower() == "pm":
        if hour < 12:
            hour += 12
        if hour == 12:
            hour = 0

    with open(BABY_NAME_FILE) as f:
        BABY_NAME = f.readline()[:-1]
    DATABASE = BABY_NAME.lower() + "-feedings.txt"

    # now = datetime.now() - timedelta(hours=1, minutes=0)
    now = datetime.now()
   
    if hour != "--":
        now = now.replace(hour=hour)
    if minute != "--":
        now = now.replace(minute=minute)

    date_time = now.strftime("%m,%d,%Y,%H,%M\n")

    with open(DATABASE, 'a') as f:
        f.write(date_time)

    print("Last feeding: " + date_time)

if __name__ == "__main__":
    main()

