#!/bin/bash

printf "Content-Type: text/plain\n\n"
sentence=$(./feed-report.py)
node speak-feeding.js "$sentence"
printf "$sentence\n"

