#!/usr/bin/env python3

import cgitb
cgitb.enable()
from datetime import datetime, timedelta

print("Content-Type: text/plain\n")

# now = datetime.now() - timedelta(hours=1, minutes=0)
now = datetime.now()
date_time = now.strftime("%m,%d,%Y,%H,%M\n")

with open('celeste-feedings.txt', 'a') as f:
    f.write(date_time)

print("Last feeding: " + date_time)

