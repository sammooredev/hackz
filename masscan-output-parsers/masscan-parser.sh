#!/bin/bash

ports=$(cat $1 | awk '{print $4}' | cut -d / -f 1)

ips=$(cat $1 | awk '{print $6}' | sed 's/$/:/')

combined=$(paste <(echo "$ips") <(echo "$ports") | sed -r 's/\s+//g')

printf "$combined\n"
