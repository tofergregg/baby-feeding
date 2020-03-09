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
    
    with open(BABY_NAME_FILE) as f:
        BABY_NAME = f.readline()[:-1]
    DATABASE = BABY_NAME.lower() + "-feedings.txt"
    

    try:
        form = json.loads(sys.stdin.read())
    except json.decoder.JSONDecodeError:
        form = {} 
   
    print(form)
    try:
        hour = form['hour']
        minute = form['minute']
        meridian = form['meridian']
        month = int(form['month'])
        day = int(form['day'])
    except KeyError:
        hour = "--" 
        minute = "--"
        meridian = "--"
        month = -1
        day = -1

    if hour != "--":
        hour = int(hour)
    if minute != "--":
        minute = int(minute)

    if meridian.lower() == "pm":
        if hour < 12:
            hour += 12
    else:
        if hour == 12:
            hour = 0

    now = datetime.now()
   
    if hour != "--":
        now = now.replace(hour=hour)
    if minute != "--":
        now = now.replace(minute=minute)

    if month != -1:
        now = now.replace(month=month)

    if day != -1:
        now = now.replace(day=day)

    date_time = now.strftime("%m,%d,%Y,%H,%M\n")

    with open(DATABASE, 'a') as f:
        f.write(date_time)

    print("Last feeding: " + date_time)

if __name__ == "__main__":
    main()

